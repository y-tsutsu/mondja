"""
Definition of urls for mondja.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as authviews
from django.conf import settings
from django.views.generic import RedirectView
from django.views import static
admin.autodiscover()

from mondja import settings
from mondja import dumpdata
from app import views as appviews

urlpatterns = patterns('',
    # Home:
    url(r'^$', appviews.home, name='home'),

     # Add:
    url(r'^add/$', appviews.add_memo, name = 'add_memo'),

    # Edit:
    url(r'^edit/(?P<id>.*)/$', appviews.edit_memo, name = 'edit_memo'),

    # Delete:
    url(r'^delete/(?P<id>.*)/$', appviews.delete_memo, name = 'delete_memo'),

    # Refresh:
    url(r'^refresh/$', appviews.refresh_memo, name = 'refresh_memo'),

    # Dumpdata:
    url(r'^dumpdata/(?P<app_name>.*)/$', dumpdata.dumpdata_app, name = 'dumpdata_app'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # MEDIA_ROOT
    (r'media/(?P<path>.*)$', static.serve, { 'document_root': settings.MEDIA_ROOT }),

    # favicon
    url(r'^favicon\.ico$', RedirectView.as_view(url = '/static/images/favicon.ico')),

    # Log-in:
    url(r'^login/$',
        authviews.login,
        {
            'template_name': 'login.html',
        },
        name = 'login'),

    # Log-out:
    url(r'^logout/$',
        authviews.logout,
        {
            'template_name': 'logout.html',
            'next_page': '../login/'
        },
        name = 'logout'),

    # python social auth
    url(r'', include('social.apps.django_app.urls', namespace='social')),
)
