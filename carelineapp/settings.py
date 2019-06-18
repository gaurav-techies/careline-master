from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting

import django.db.models.options as options

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('description',)


