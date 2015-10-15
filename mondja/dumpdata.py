from django.shortcuts import *
from django.http import HttpRequest
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
import subprocess

dir = settings.MEDIA_ROOT

@user_passes_test(lambda u: u.is_staff)
def dumpdata_app(request, app_name):
    """appのDBのエクスポートを行う．"""
    p = subprocess.Popen(['python', 'manage.py', 'dumpdata', app_name, '--format=json', '--indent=2'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = False)
    stdout, stderr = p.communicate()

    filename = dir + '/' + app_name + '.json'
    with open(filename, 'wb') as f:
        f.write(stdout)

    return HttpResponseRedirect(settings.MEDIA_URL + app_name + '.json')
