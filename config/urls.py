from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

from leads import urls as lead_urls
from sms_messaging import urls as sms_messaging_urls
from wagtail.contrib.sitemaps.views import sitemap

from django.views.generic import TemplateView

from search import views as search_views

from .api import api_router

adminurlkey = str(r'^{}/').format(settings.WAGTAIL_URLKEY)

urlpatterns = [
    # url(r'^django-admin/', include(admin.site.urls)),
    url(adminurlkey, include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^leads/', include(lead_urls)),

    url(r'^careapi/v2/', include('api.urls')),

    url(r'^search/$', search_views.search, name='search'),

    url(r'^message-center/', include(sms_messaging_urls)),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:]
    url('^sitemap\.xml$', sitemap),

    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^callback\.html$', TemplateView.as_view(template_name='callback.html', content_type='text/plain')),

    url(r'^api/v2/', api_router.urls),

    url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
