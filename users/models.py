from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
import re

# Sydney Postcode Validation
def validate_sydney_postcode(value):
    regex = re.compile(
        r'^[2][0-9]{3}$', re.IGNORECASE)

    regex = re.compile(regex)
    if not regex.match(value):
        raise ValidationError(u'%s CCareline helps Sydneysiders navigate the maze of social services and makes referrals '
                              u'to counsellors, therapists and case managers across Sydney. This app is not intended for '
                              u'use outside Sydney.' % value)

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class AutoNowAdd(models.Model):
    created_time = models.DateTimeField('created_at', auto_now_add=True)
    updated_time = models.DateTimeField('updated_at', auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):

    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = CharField(_("First Name of User"), blank=True, max_length=255)
    last_name = CharField(_("Last Name of User"), blank=True, max_length=255)
    organisation = CharField(_("Organisation of User"), blank=True, null=True, max_length=255)
    postcode = CharField(validators=[validate_sydney_postcode], blank=True, max_length=7)
    mobile = models.IntegerField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Tracking(AutoNowAdd):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tracking')
    landed_time = models.DateTimeField('landed_at', null=True, blank=True)
    apilevel = models.IntegerField(null=True, blank=True)
    application_name = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    build_number = models.IntegerField(null=True, blank=True)
    bundle_id = models.CharField(max_length=255, null=True, blank=True)
    carrier = models.CharField(max_length=255, null=True, blank=True)
    device_country = models.CharField(max_length=10, null=True, blank=True)
    device_id = models.CharField(max_length=255, null=True, blank=True)
    device_token = models.CharField(max_length=255, null=True, blank=True)
    device_locale = models.CharField(max_length=20, null=True, blank=True)
    device_name = models.CharField(max_length=255, null=True, blank=True)
    first_install_time = models.BigIntegerField(null=True, blank=True)
    font_scale = models.DecimalField(max_digits=100, decimal_places=30, null=True, blank=True)
    free_disk_storage = models.BigIntegerField(null=True, blank=True)
    ip_address = models.CharField(max_length=20, null=True, blank=True)
    install_referrer = models.CharField(max_length=255, null=True, blank=True)
    instance_id = models.CharField(max_length=255, null=True, blank=True)
    last_update_time = models.CharField(max_length=255, null=True, blank=True)
    mac_address = models.CharField(max_length=255, null=True, blank=True)
    manufacturer = models.CharField(max_length=255, null=True, blank=True)
    max_memory = models.IntegerField(null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    readable_version = models.CharField(max_length=20, null=True, blank=True)
    serial_number = models.CharField(max_length=255, null=True, blank=True)
    system_name = models.CharField(max_length=255, null=True, blank=True)
    system_version = models.CharField(max_length=255, null=True, blank=True)
    timezone = models.CharField(max_length=100, null=True, blank=True)
    total_disk_capacity = models.BigIntegerField(null=True, blank=True)
    total_memory = models.BigIntegerField(null=True, blank=True)
    unique_id = models.CharField(max_length=100)
    useragent = models.CharField(max_length=1000, null=True, blank=True)
    version = models.CharField(max_length=100, null=True, blank=True)
    twenty_four_hour = models.BooleanField(default=False)
    emulator = models.BooleanField(default=False)
    pin_or_fingerprint_set = models.BooleanField(default=False)
    tablet = models.BooleanField(default=False)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    ticket_ref = models.CharField(null=True,max_length=30)
    push = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"email": self.email})