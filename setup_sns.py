import django

django.setup()

from scarface.models import Application, Platform, Topic
from django.conf import settings
from django.db import IntegrityError


def setup_application():
    try:
        app = Application.objects.create(name='ccareline')
    except IntegrityError:
        app = Application.objects.get(name='ccareline')
        pass
    return app


def setup_apple_platform(app):
    try:
        Platform.objects.get_or_create(
            platform='APNS', application=app, arn=settings.PUSH_APPLE
        )
    except IntegrityError:
        pass


def setup_android_platform(app):
    android_arn = settings.PUSH_ANDROID if hasattr(settings, 'PUSH_ANDROID') else 'xyz'
    try:
        Platform.objects.get_or_create(
            platform='GCM', application=app, arn=android_arn
        )
    except IntegrityError:
        pass


def setup_topic(app):
    topic, created = Topic.objects.get_or_create(name='push_notifications', application=app)
    try:
        topic.register()
    except:
        pass


app = setup_application()
setup_apple_platform(app)
setup_android_platform(app)
setup_topic(app)