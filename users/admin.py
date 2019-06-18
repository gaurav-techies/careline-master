from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(ModelAdmin):
    model = User
    fieldsets = (("User", {"fields": ("first_name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["email", "first_name", "is_superuser"]
    search_fields = ["first_name", "email", "mobile", "organisation", "postcode", ]

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(UserAdmin)