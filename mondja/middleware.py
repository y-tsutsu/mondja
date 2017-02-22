from mondja.pydenticon_wrapper import create_identicon
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

class MondjaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before

        # Heroku用にidenticonを生成
        users = User.objects.all()
        for item in users:
            if item.username != '':
                create_identicon(item.username)


        response = self.get_response(request)

        # Code to be executed for each request/response after

        return response
