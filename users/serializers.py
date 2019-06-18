from rest_framework import serializers
from . import models


class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tracking
        fields = (
            "landed_time",
            "apilevel",
            "application_name",
            "brand",
            "build_number",
            "bundle_id",
            "carrier",
            "device_country",
            "device_id",
            "device_token",
            "device_locale",
            "device_name",
            "first_install_time",
            "font_scale",
            "free_disk_storage",
            "ip_address",
            "install_referrer",
            "instance_id",
            "last_update_time",
            "mac_address",
            "manufacturer",
            "max_memory",
            "model",
            "phone_number",
            "readable_version",
            "serial_number",
            "system_name",
            "system_version",
            "timezone",
            "total_disk_capacity",
            "total_memory",
            "unique_id",
            "useragent",
            "version",
            "twenty_four_hour",
            "emulator",
            "pin_or_fingerprint_set",
            "tablet",
            "latitude",
            "longitude",
            "push",
        )
        read_only_fields = ("ticket_ref", )
        abstract = True

    def get_or_create(self, user, ticket_ref):
        defaults = self.validated_data.copy()
        identifier = defaults.pop('unique_id')
        tracking, created = models.Tracking.objects.get_or_create(
            unique_id=identifier, user=user
        )
        if created:
            for attr, value in defaults.items():
                setattr(tracking, attr, value)
            tracking.ticket_ref = ticket_ref
            tracking.save()
        return tracking, created


class UserSerializer(TrackingSerializer):
    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'mobile', 'organisation', 'postcode', )


class DeviceSerializer(serializers.Serializer):
    device_token = serializers.CharField(max_length=160, required=False)
    push = serializers.BooleanField(required=True)
    unique_id = serializers.CharField(max_length=400, required=True)