from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import PushNotify



class PushNotifyAdmin(ModelAdmin):
    model = PushNotify
    menu_label = 'Push Notifications'
    list_display = ('msg', 'created_at', )


modeladmin_register(PushNotifyAdmin)