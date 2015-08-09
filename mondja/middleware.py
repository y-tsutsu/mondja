from mondja.pydenticon_wrapper import create_identicon

class MondjaMiddleware:

    def process_request(self, request):
        ''' リクエストごとにDjangoがどのビューを実行するか決定する前に呼び出されます．'''

        if request.user.username != '':
            create_identicon(request.user.username)
