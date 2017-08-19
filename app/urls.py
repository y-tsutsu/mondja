"""nyanpasu_svr URL Configuration

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
from django.conf.urls import url
from . import views

urlpatterns = [
    # Home:
    url(r'^$', views.home, name='home'),

    # Add:
    url(r'^add/$', views.add_memo, name='add_memo'),

    # Edit:
    url(r'^edit/(?P<id>.*)/$', views.edit_memo, name='edit_memo'),

    # Delete:
    url(r'^delete/(?P<id>.*)/$', views.delete_memo, name='delete_memo'),

    # Refresh:
    url(r'^refresh/$', views.refresh_memo, name='refresh_memo'),
]
