"""mondja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views import static
from django.views.generic import RedirectView
from mondja import settings
from mondja import dumpdata
from app import urls as appurls
from social_django import urls as sclurls

admin.autodiscover()

urlpatterns = [
    # app
    url(r'', include(appurls)),

    # Dumpdata:
    url(r'^dumpdata/(?P<app_name>.*)/$',
        dumpdata.dumpdata_app, name='dumpdata_app'),

    # Log-in:
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),

    # Log-out:
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # MEDIA_ROOT
    url(r'media/(?P<path>.*)$', static.serve,
        {'document_root': settings.MEDIA_ROOT}),

    # favicon
    url(r'^favicon\.ico$', RedirectView.as_view(
        url='/static/images/favicon.ico')),

    # python social auth
    url(r'', include(sclurls, namespace='social')),
]
