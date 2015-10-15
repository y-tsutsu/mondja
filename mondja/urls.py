"""
Definition of urls for mondja.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView
admin.autodiscover()

from mondja import settings

urlpatterns = patterns('',
    # Home:
    url(r'^$', 'app.views.home', name='home'),

     # Add:
    url(r'^add/$', 'app.views.add_memo', name = 'add_memo'),

    # Edit:
    url(r'^edit/(?P<id>.*)/$', 'app.views.edit_memo', name = 'edit_memo'),

    # Delete:
    url(r'^delete/(?P<id>.*)/$', 'app.views.delete_memo', name = 'delete_memo'),

    # Refresh:
    url(r'^refresh/$', 'app.views.refresh_memo', name = 'refresh_memo'),

    # Dumpdata:
    url(r'^dumpdata/(?P<app_name>.*)/$', 'mondja.dumpdata.dumpdata_app', name = 'dumpdata_app'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # MEDIA_ROOT
    (r'media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),

    # favicon
    url(r'^favicon\.ico$', RedirectView.as_view(url = '/static/images/favicon.ico')),

    # Log-in:
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'login.html',
        },
        name = 'login'),

    # Log-out:
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        {
            'template_name': 'logout.html',
            'next_page': '../login/'
        },
        name = 'logout'),
)
