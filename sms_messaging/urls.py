from django.conf.urls import url
from . import views


from django.contrib import admin
admin.autodiscover()

urlpatterns = (
#    url(r'^sms/$', views.sms, name='sms'),
    # url(r'^ring/$', views.ring, name='ring'),
)