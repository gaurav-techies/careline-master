# Generated by Django 2.0.8 on 2018-12-08 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='First Name of User')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='Last Name of User')),
                ('organisation', models.CharField(blank=True, max_length=255, null=True, verbose_name='Organisation of User')),
                ('postcode', models.CharField(blank=True, max_length=7, validators=[users.models.validate_sydney_postcode])),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('landed_time', models.DateTimeField(blank=True, null=True, verbose_name='landed_at')),
                ('apilevel', models.IntegerField(blank=True, null=True)),
                ('application_name', models.CharField(blank=True, max_length=255, null=True)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('build_number', models.IntegerField(blank=True, null=True)),
                ('bundle_id', models.CharField(blank=True, max_length=255, null=True)),
                ('carrier', models.CharField(blank=True, max_length=255, null=True)),
                ('device_country', models.CharField(blank=True, max_length=10, null=True)),
                ('device_id', models.CharField(blank=True, max_length=255, null=True)),
                ('device_token', models.CharField(blank=True, max_length=255, null=True)),
                ('device_locale', models.CharField(blank=True, max_length=20, null=True)),
                ('device_name', models.CharField(blank=True, max_length=255, null=True)),
                ('first_install_time', models.BigIntegerField(blank=True, null=True)),
                ('font_scale', models.DecimalField(blank=True, decimal_places=30, max_digits=100, null=True)),
                ('free_disk_storage', models.BigIntegerField(blank=True, null=True)),
                ('ip_address', models.CharField(blank=True, max_length=20, null=True)),
                ('install_referrer', models.CharField(blank=True, max_length=255, null=True)),
                ('instance_id', models.CharField(blank=True, max_length=255, null=True)),
                ('last_update_time', models.CharField(blank=True, max_length=255, null=True)),
                ('mac_address', models.CharField(blank=True, max_length=255, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=255, null=True)),
                ('max_memory', models.IntegerField(blank=True, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('readable_version', models.CharField(blank=True, max_length=20, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=255, null=True)),
                ('system_name', models.CharField(blank=True, max_length=255, null=True)),
                ('system_version', models.CharField(blank=True, max_length=255, null=True)),
                ('timezone', models.CharField(blank=True, max_length=100, null=True)),
                ('total_disk_capacity', models.BigIntegerField(blank=True, null=True)),
                ('total_memory', models.BigIntegerField(blank=True, null=True)),
                ('unique_id', models.CharField(max_length=100)),
                ('useragent', models.CharField(blank=True, max_length=1000, null=True)),
                ('version', models.CharField(blank=True, max_length=100, null=True)),
                ('twenty_four_hour', models.BooleanField(default=False)),
                ('emulator', models.BooleanField(default=False)),
                ('pin_or_fingerprint_set', models.BooleanField(default=False)),
                ('tablet', models.BooleanField(default=False)),
                ('latitude', models.CharField(blank=True, max_length=20, null=True)),
                ('longitude', models.CharField(blank=True, max_length=20, null=True)),
                ('ticket_ref', models.CharField(max_length=30, null=True)),
                ('push', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tracking', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
