from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import LeadDB


class LeadAdmin(ModelAdmin):
    model = LeadDB
    list_display = ["user", "recipient_contact_name", "recipient_contact_number", "bitly_link",]
    search_fields = ["recipient_contact_name", ]

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(LeadAdmin)