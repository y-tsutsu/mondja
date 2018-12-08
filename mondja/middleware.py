from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from mondja.pydenticon_wrapper import create_identicon


class MondjaMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_request(self, request):
        # Heroku用にidenticonを生成
        users = User.objects.all()
        for item in users:
            if item.username != '':
                create_identicon(item.username)

        # ログインしている状態でloginページがリクエストされた場合はHomeにredirectする
        if request.path == reverse('login') and request.method == 'GET' and request.user.is_authenticated:
            # 例外としてuser_passes_test(is_staff)でredirectされた場合はHomeにredirectしない
            if request.GET.get('need_staff') and not request.user.is_staff:
                pass
            # 例外としてuser_passes_test(is_superuser)でredirectされた場合はHomeにredirectしない
            elif request.GET.get('need_superuser') and not request.user.is_superuser:
                pass
            # そのほかの場合はHomeにredirectする
            else:
                return redirect('/')
