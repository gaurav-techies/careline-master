from __future__ import absolute_import
from templated_email import send_templated_mail
from taskapp.celery import app

from django.conf import settings
from scarface.models import Topic, Platform, Device
from .models import User, Tracking

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
def create_zoho_signup_lead(user_id, tracking_id):
    users = User.objects.get(id=user_id)
    tracking = Tracking.objects.get(id=tracking_id)

    refresh_token = settings.REFRESH_TOKEN
    api_domain = settings.API_DOMAIN
    account_id = settings.ACCOUNT_ID

    # Convert django database datetime to Zoho CRM Datetime format
    time_raw = tracking.landed_time
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
                    "Lead_Status": "New Mobile App Sign-up",
                    "First_Name": users.first_name,
                    "Last_Name": users.last_name,
                    "Mobile": users.mobile,
                    "Presenting_Problem": lead.careline_topic.title,
                    "Referal_Time": time_clean_zoho_format,
                    'build_number': tracking.build_number,
                    "Callback_Permission": bool(lead.callback_permission),
                    "Recipient_Permission": bool(lead.recipient_permission),
                    "Bitly_Link": bitly_link_str,
            }
        ]
    }

    jsondata = json.dumps(data)
    print(jsondata)

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
def send_email_upon_signup(user_id, tracking_id):
    users = User.objects.get(id=user_id)
    tracking = Tracking.objects.get(id=tracking_id)

    from_email = settings.DEFAULT_FROM_EMAIL
    recipients = ['connect@catholiccare.org']

    return send_templated_mail(
        template_name='users-email-ticket',
        from_email=from_email,
        recipient_list=recipients,
        context={
            'user': users.email,
            'first_name': users.first_name,
            'last_name': users.last_name,
            'mobile': users.mobile,
            'landed_time': tracking.landed_time,
            'carrier': tracking.carrier,
            'ip_address': tracking.ip_address,
            'system_name': tracking.system_name,
            'unique_id': tracking.unique_id,
            'manufacturer': tracking.manufacturer,
            'ticket_ref': tracking.ticket_ref,
        }
    )


@app.task
def device_register(tracking_id):
    tracking = Tracking.objects.get(id=tracking_id)

    # register push device
    if tracking.system_name == 'iOS':
        platform = Platform.objects.get(platform='APNS')
    else:
        platform = Platform.objects.get(platform='GCM')

    topic = Topic.objects.get(name='push_notifications')
    device, created = Device.objects.get_or_create(device_id=tracking.unique_id, platform=platform)
    device.push_token = tracking.device_token
    device.save()

    try:
        device.register()
        topic.register_device(device)
    except:
        pass
