from django.conf import settings

def enabled_social_auth(request):
    return {'ENABLED_SOCIAL_AUTH': settings.ENABLED_SOCIAL_AUTH}
