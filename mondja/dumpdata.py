from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.core.management import call_command
from django.shortcuts import HttpResponseRedirect


@user_passes_test(lambda u: u.is_staff, login_url=f'/{settings.LOGIN_URL}?need_staff=True')
def dumpdata_app(request, app_name):
    '''appのDBのエクスポートを行う．'''
    filename = f'{settings.MEDIA_ROOT / app_name}.json'
    with open(filename, 'w') as output:
        call_command('dumpdata', app_name, format='json', indent=2, stdout=output)

    return HttpResponseRedirect(settings.MEDIA_URL + app_name + '.json')
