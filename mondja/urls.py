﻿"""
Definition of urls for mondja.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Home:
    url(r'^$', 'app.views.home', name='home'),

     # Add:
    url(r'^add/$', 'app.views.add_memo', name = 'add_memo'),

    # Edit:
    url(r'^edit/(?P<id>.*)/$', 'app.views.edit_memo', name = 'edit_memo'),

    # Delete:
    url(r'^delete/(?P<id>.*)/$', 'app.views.delete_memo', name = 'delete_memo'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

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
