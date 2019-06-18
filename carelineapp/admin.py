from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import SMSTemplate, Topic

# class SMSTemplateAdmin(ModelAdmin):
#     model = SMSTemplate

class SMSTemplateAdmin(ModelAdmin):
    model = SMSTemplate
    menu_label = 'SMS Template'  # ditch this to use verbose_name_plural from model
    menu_icon = 'mail'  # change as required
    menu_order = 600  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    list_display = ('from_sms', 'text')
    list_filter = ('from_sms', 'text')
    search_fields = ('text',)

class TopicAdmin(ModelAdmin):
    model = Topic
    menu_label = 'Topics'  # ditch this to use verbose_name_plural from model
    menu_icon = 'tag'  # change as required
    menu_order = 500  # will put in 4th place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    list_display = ('topic_id', 'title', 'counselling_topic')
    list_filter = ('title', 'counselling_topic')
    search_fields = ('title', )

modeladmin_register(SMSTemplateAdmin)
modeladmin_register(TopicAdmin)
