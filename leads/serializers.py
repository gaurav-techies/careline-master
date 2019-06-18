from rest_framework import serializers
import random
import time

from .models import Tracking, LeadDB
from .tasks import send_sms, send_email_upon_registration, create_zoho_refer_lead

def ticket_ref_generator():
    rng = random.SystemRandom(45645 * time.time())
    ticket_ref = [str(rng.randint(0, 9)) for i in range(10)]
    ticket_ref = ''.join(ticket_ref)

    return ticket_ref

class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = ("latitude",
                  "longitude",
                  )
        read_only_fields = ("ticket_ref", )
        abstract = True


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadDB
        fields = (
            'recipient_contact_name',
            'recipient_contact_number',
            'callback_permission',
            'recipient_permission',
            'careline_topic',
            'referral_text_message_reason',
            'date_time_referral'
        )

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        lead = super().create(validated_data)
        topic = lead.careline_topic
        bitly_url = topic.bitly_url
        lead.ticket_ref = ticket_ref_generator()
        lead.bitly_link = bitly_url
        lead.user = user
        lead.save()

        if lead.recipient_permission:
            # send sms send_sms_function
            send_sms.delay(lead.pk)
            # send email ticket function
            send_email_upon_registration.delay(lead.pk)
            # send lead to Zoho crm
            create_zoho_refer_lead.delay(lead.pk)
        return lead
