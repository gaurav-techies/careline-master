from __future__ import absolute_import
from templated_email import send_templated_mail
from taskapp.celery import app

from django.conf import settings
from twilio.rest import Client

from leads.models import LeadDB

from django.core import serializers
import requests
import os
import environ
import credstash
import json
import re
import datetime
from json import JSONEncoder

def generate_access_token(refresh_token):
    accounts_url = settings.ACCOUNTS_URL
    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET
    refresh_token = settings.REFRESH_TOKEN

    refresh_url = "/oauth/v2/token"
    url = accounts_url + refresh_url

    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }

    r = requests.post(url, params=params)
    if r.status_code == 200:
        return r.json()['access_token']
    else:
        raise Exception('Cant get access token')


@app.task
def create_zoho_refer_lead(lead_id):
    lead = LeadDB.objects.get(pk=lead_id)

    refresh_token = settings.REFRESH_TOKEN
    api_domain = settings.API_DOMAIN
    account_id = settings.ACCOUNT_ID

    # Convert django database datetime to Zoho CRM Datetime format
    time_raw = lead.date_time_referral
    time_clean_zoho_format = time_raw.isoformat(timespec='seconds')

    influencer_full_name = lead.user.first_name + ' ' + lead.user.last_name

    bitly_link_str = str(lead.bitly_link or "https://ccareline.app/#")

    phone_no_zero = str(lead.user.mobile)
    phone_string = str('{}' + phone_no_zero).format('0')

    url = "{}/crm/v2/Leads".format(api_domain)
    tkn = generate_access_token(refresh_token)
    data = {
        "data": [
            {
                "Owner": {
                    "id": "{}".format(account_id)
                },
                    "Ticket_Ref": lead.ticket_ref,
                    "Lead_Status": "Referer CCarelineApp Lead",
                    "First_Name": lead.recipient_contact_name,
                    "Last_Name": "*",
                    "Email_Opt_Out": False,
                    "SMS_referrer": False,
                    "Lead_Stage": "Mobile App Referer",
                    "Mobile": lead.recipient_contact_number,
                    "UTM_Lead_Source": 'Mobile App Referer',
                    "Presenting_Problem": lead.careline_topic.title,
                    "Referal_Time": time_clean_zoho_format,
                    "Community_Influencer_Details": influencer_full_name,
                    "Community_Influencer_Email": lead.user.email,
                    "Community_Influencer_Mobile": phone_string,
                    "Communit_Influencer_Organisation": lead.user.organisation,
                    "Community_Influencer_Postcode": lead.user.postcode,
                    "Callback_Permission": bool(lead.callback_permission),
                    "Recipient_Permission": bool(lead.recipient_permission),
                    "Bitly_Link": bitly_link_str,
            }
        ]
    }

    jsondata = json.dumps(data)
    # print(jsondata)

    headers = {
        'Authorization': "Zoho-oauthtoken {}".format(tkn),
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
    }

    response = requests.post(url, data=jsondata, headers=headers)

    if response.status_code == 201:
        return True
    else:
        raise Exception('Cant create a record')

@app.task
def send_email_upon_registration(lead_id):
    lead = LeadDB.objects.get(pk=lead_id)

    from_email = settings.DEFAULT_FROM_EMAIL

    recipients = ['connect@catholiccare.org']

    bitly_link_str = lead.bitly_link or "https://ccareline.app/#"

    return send_templated_mail(
        template_name='lead-email-ticket',
        from_email=from_email,
        recipient_list=recipients,
        context={
            'user': lead.user,
            'careline_topic': lead.careline_topic,
            'ticket_ref': lead.ticket_ref,
            'date_time_referral': lead.date_time_referral,
            'recipient_contact_name': lead.recipient_contact_name,
            'recipient_contact_number': lead.recipient_contact_number,
            'referral_text_message_reason': lead.referral_text_message_reason,
            'callback_permission': str(lead.callback_permission),
            'recipient_permission': str(lead.recipient_permission),
            "community_influencer_name": lead.user.first_name,
            "community_influencer_details": lead.user,
            "community_influencer_mobile": lead.user.mobile,
            'bitly_link': str(bitly_link_str),
        }
    )


@app.task
def send_sms(lead_id):
    lead = LeadDB.objects.get(pk=lead_id)
    topic = lead.careline_topic
    # get the topic
    # Default URL if Bitly Fails
    bitly_link_str = lead.bitly_link or "https://ccareline.app/#"
    body = topic.get_sms_template(lead.recipient_contact_name, bitly_link_str)

    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    # Strip (0) from beginning of number the append +61 at start
    s = lead.recipient_contact_number
    mnumber = '+61{}'.format(s[1:] if s.startswith('0') else s)

    message = client.messages.create(
        to=mnumber,
        # from_='CCARELINE',
        from_='+61488839814',
        body=body,
    )

    lead.twilio_sms_sid = message.sid
    lead.save()
    return