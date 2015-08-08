"""
Definition of urls for mondja.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Home:
    url(r'^$', 'app.views.home', name='home'),

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

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
