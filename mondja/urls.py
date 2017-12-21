"""mondja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import static, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.urls import include, path
from django.views.generic import RedirectView
from social_django import urls as sclurls

from . import dumpdata, settings

urlpatterns = [
    # app
    path('', include('app.urls')),

    # Dumpdata:
    path('dumpdata/<str:app_name>/', dumpdata.dumpdata_app, name='dumpdata_app'),

    # Log-in:
    path('login/', login, {'template_name': 'login.html'}, name='login'),

    # Log-out:
    path('logout/', logout, {'next_page': '/'}, name='logout'),

    # Admin Doc
    path('admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin
    path('admin/', admin.site.urls),

    # MEDIA_ROOT
    url(r'media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),

    # favicon
    path('favicon.ico', RedirectView.as_view(
        url='/static/images/favicon.ico', permanent=True)),

    # python social auth
    path('', include('social_django.urls', namespace='social')),
]
