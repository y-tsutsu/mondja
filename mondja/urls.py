"""mondja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path, re_path
from django.views.generic import RedirectView

from . import dumpdata

urlpatterns = [
    # app
    path('', include('app.urls')),

    # Dumpdata:
    path('dumpdata/<str:app_name>/', dumpdata.dumpdata_app, name='dumpdata_app'),

    # Log-in:
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    # Log-out:
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    # Admin Doc
    path('admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin
    path('admin/', admin.site.urls),

    # MEDIA_ROOT
    re_path(r'media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),

    # favicon
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)),

    # python social auth
    path('', include('social_django.urls', namespace='social')),
]
