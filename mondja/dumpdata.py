from django.shortcuts import *
from django.http import HttpRequest
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.core.management import call_command

@user_passes_test(lambda u: u.is_staff)
def dumpdata_app(request, app_name):
    """appのDBのエクスポートを行う．"""
    filename = settings.MEDIA_ROOT + '/' + app_name + '.json'
    with open(filename, 'w') as output:
        call_command('dumpdata', app_name, format = 'json', indent = 2, stdout = output)

    return HttpResponseRedirect(settings.MEDIA_URL + app_name + '.json')
