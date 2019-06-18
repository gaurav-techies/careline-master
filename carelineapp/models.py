from __future__ import absolute_import, unicode_literals
from wagtail.contrib.settings.models import BaseSetting

from wagtailmetadata.models import MetadataPageMixin
from taggit.models import TaggedItemBase
from django.conf import settings

import django.db.models.options as options

from modelcluster.contrib.taggit import ClusterTaggableManager

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('description', )
from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
import requests

from wagtail.api import APIField
import random

# SMS Template Sending Models
class SMSTemplate(models.Model):
    text = models.CharField(
        max_length=160,
        help_text=("Add {{topic_title}} for Name of Topic and {{name}} for Name of recipient /"
                   "and {{link}} for the service pdf bitly link")
    )
    from_sms = models.CharField(
        max_length=10
    )

    def __str__(self):
        return self.from_sms



# Topic Page Models
class Topic(models.Model):
    topic_id = models.IntegerField(
        help_text='Topic ID must be unique',
        unique=True
    )
    title = models.CharField(
        help_text='Title of counselling topic',
        max_length=65
    )
    introduction = models.CharField(
        help_text='Introduction heading of counselling topic',
        max_length=300
    )
    counselling_topic = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    custom_url = models.URLField(
        help_text='Custom URL',
        max_length=200,
        null=True, blank=True
    )

    def __str__(self):
        return self.title

    @property
    def bitly_url(self):
        bitly_url = "https://api-ssl.bitly.com/v4/bitlinks"

        if self.counselling_topic:
            body = {"long_url": "{}#{}".format(
                self.counselling_topic.file.url, random.randint(1, 99999)
            )}
            header = {"Authorization": "Bearer {}".format(settings.BITLY_ACCESS_TOKEN)}
            short_url = requests.post(bitly_url, headers=header, json=body)
            return short_url.json().get('link')

        return bitly_url

    def get_sms_template(self, name, bitly_link):
        template = SMSTemplate.objects.get(id=1).text # the sms template will always be stored on id =1
        template = template.replace("{{topic_title}}", self.title)
        template = template.replace("{{name}}", name)
        template = template.replace("{{link}}", bitly_link)
        return template

# Basic Page Models
class BasicPageTag(TaggedItemBase):
    content_object = ParentalKey('carelineapp.BasicPage', related_name='tagged_items')


class BasicPage(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    tags = ClusterTaggableManager(through=BasicPageTag, blank=True)

    body = RichTextField(blank=True, features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'blockquote', 'phone_link', 'link', 'document-link', 'image', 'bold', 'italic'])

    # Export fields over the API
    api_fields = [
        APIField('author'),
        APIField('date'),
        APIField('tags'),
        APIField('body'),
    ]
    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
    ]
    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('body'),
    ]

# Refer a Friend Page Models
class ReferFriendPageTag(TaggedItemBase):
    content_object = ParentalKey('carelineapp.ReferFriendPage', related_name='tagged_items')
class ReferFriendPage(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    tags = ClusterTaggableManager(through=ReferFriendPageTag, blank=True)

    action_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="send to a friends phone",
        help_text='This is for the action title text on the image banner'
    )
    section_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="refer a friend",
        help_text='This is for the section name text on the image banner'
    )
    sub_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="sending topics",
        help_text='This is for the subtitle text on the image banner'
    )
    helper_text_one = RichTextField(blank=True, null=True)
    helper_text_two = RichTextField(blank=True, null=True)

    # Export fields over the API
    api_fields = [
        APIField('author'),
        APIField('date'),
        APIField('tags'),
        APIField('action_title'),
        APIField('section_name'),
        APIField('sub_title'),
        APIField('helper_text_one'),
        APIField('helper_text_two'),
    ]
    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
    ]
    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('action_title'),
        FieldPanel('section_name'),
        FieldPanel('sub_title'),
        FieldPanel('helper_text_one'),
        FieldPanel('helper_text_two'),
    ]

# Support us Page Models
class SupportUsPageTag(TaggedItemBase):
    content_object = ParentalKey('carelineapp.SupportUsPage', related_name='tagged_items')
class SupportUsPage(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    tags = ClusterTaggableManager(through=ReferFriendPageTag, blank=True)

    action_title = models.CharField(max_length=255, blank=True, default="text to come")
    section_name = models.CharField(max_length=255, blank=True, default="support us")
    sub_title = models.CharField(max_length=255, blank=True, default="text to come")

    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
    ]
    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('action_title'),
        FieldPanel('section_name'),
        FieldPanel('sub_title'),
    ]

# Contact us Page Models
class ContactUsPageTag(TaggedItemBase):
    content_object = ParentalKey('carelineapp.ContactUsPage', related_name='tagged_items')
class ContactUsPage(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    tags = ClusterTaggableManager(through=ContactUsPageTag, blank=True)

    phone_number = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # Export fields over the API
    api_fields = [
        APIField('author'),
        APIField('date'),
        APIField('tags'),
        APIField('phone_number'),
        APIField('email'),
    ]
    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
    ]
    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('phone_number'),
        FieldPanel('email'),
    ]

# Signup Page models
class SignupPageTag(TaggedItemBase):
    content_object = ParentalKey('carelineapp.SignupPage', related_name='tagged_items')
class SignupPage(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    tags = ClusterTaggableManager(through=SignupPageTag, blank=True)

    first_name_helper_text = RichTextField(blank=True, null=True)
    last_name_helper_text = RichTextField(blank=True, null=True)
    email_helper_text = RichTextField(blank=True, null=True)
    mobile_helper_text = RichTextField(blank=True, null=True)
    organisation_helper_text = RichTextField(blank=True, null=True)
    postcode_helper_text = RichTextField(blank=True, null=True)
    password_helper_text = RichTextField(blank=True, null=True)
    agree_terms_helper_text = RichTextField(blank=True, null=True)

    # Export fields over the API
    api_fields = [
        APIField('author'),
        APIField('date'),
        APIField('tags'),
        APIField('first_name_helper_text'),
        APIField('last_name_helper_text'),
        APIField('email_helper_text'),
        APIField('mobile_helper_text'),
        APIField('organisation_helper_text'),
        APIField('postcode_helper_text'),
        APIField('password_helper_text'),
        APIField('agree_terms_helper_text'),
    ]
    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
    ]
    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('first_name_helper_text'),
        FieldPanel('last_name_helper_text'),
        FieldPanel('email_helper_text'),
        FieldPanel('mobile_helper_text'),
        FieldPanel('organisation_helper_text'),
        FieldPanel('postcode_helper_text'),
        FieldPanel('password_helper_text'),
        FieldPanel('agree_terms_helper_text'),
    ]

# Log in Page models
class LoginPageTag(TaggedItemBase):
    content_object = ParentalKey('carelineapp.LoginPage', related_name='tagged_items')
class LoginPage(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    tags = ClusterTaggableManager(through=LoginPageTag, blank=True)

    email_helper_text = RichTextField(blank=True, null=True)
    password_helper_text = RichTextField(blank=True, null=True)
    keep_me_logged_helper_text = RichTextField(blank=True, null=True)

    # Export fields over the API
    api_fields = [
        APIField('author'),
        APIField('date'),
        APIField('tags'),
        APIField('email_helper_text'),
        APIField('password_helper_text'),
        APIField('keep_me_logged_helper_text'),
    ]
    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
    ]
    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('email_helper_text'),
        FieldPanel('password_helper_text'),
        FieldPanel('keep_me_logged_helper_text'),
    ]

# Send SMS Link Page models
class SendSmsLinkPageTag(TaggedItemBase):
    content_object = ParentalKey('carelineapp.SendSmsLink', related_name='tagged_items')
class SendSmsLink(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    tags = ClusterTaggableManager(through=SendSmsLinkPageTag, blank=True)

    name_helper_text = RichTextField(blank=True, null=True)
    friends_mobile_number_helper_text = RichTextField(blank=True, null=True)

    # Export fields over the API
    api_fields = [
        APIField('author'),
        APIField('date'),
        APIField('tags'),
        APIField('name_helper_text'),
        APIField('friends_mobile_number_helper_text'),
    ]
    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
    ]
    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('name_helper_text'),
        FieldPanel('friends_mobile_number_helper_text'),
    ]
