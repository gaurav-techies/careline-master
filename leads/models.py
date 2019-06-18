import uuid
import requests
from django.db import models
from django.conf import settings
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from carelineapp.models import Topic
from django.contrib.auth import get_user_model

User = get_user_model()


class AutoNowAdd(models.Model):
    created_time = models.DateTimeField('created_at', auto_now_add=True)
    updated_time = models.DateTimeField('updated_at', auto_now=True)

    class Meta:
        abstract = True


class Tracking(AutoNowAdd):
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    ticket_ref = models.CharField(null=True, max_length=30)


class LeadDB(Tracking):
    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Lead Analytics"

    leadid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Foreign Key
    recipient_contact_name = models.CharField(max_length=250, null=True)
    recipient_contact_number = models.CharField(max_length=20)
    careline_topic = models.ForeignKey(Topic, on_delete=models.PROTECT, related_name='leads')
    referral_text_message_reason = models.CharField(max_length=255, null=True)
    date_time_referral = models.DateTimeField(null=True)

    text_message_body = models.CharField(max_length=1000, null=True)
    callback_permission = models.BooleanField(default=False)
    recipient_permission = models.BooleanField(default=False)

    bitly_link = models.CharField(max_length=100, null=True, blank=True)
    bitly_link_clicked = models.BooleanField(default=False)
    twilio_sms_sid = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, related_name='referrer', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.recipient_contact_name

    @property
    def bitly_click(self):

        if self.bitly_link is not None and not self.bitly_link_clicked:
            bitly_link = self.bitly_link.split("/")[-1]
            bitly_url = "https://api-ssl.bitly.com/v4/bitlinks/bit.ly/{}/clicks/summary".format(bitly_link)

            body = {"unit": "month", "units": -1}
            header = {"Authorization": "Bearer {}".format(settings.BITLY_ACCESS_TOKEN)}

            short_url = requests.get(bitly_url, headers=header, params=body)

            clicks = short_url.json().get('total_clicks')

            if clicks > 0:
                self.bitly_link_clicked = True

            self.save()
        return self.bitly_link_clicked

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('bitly_link_clicked'),
            ],
            heading="Bitly Details",
        ),
    ]
