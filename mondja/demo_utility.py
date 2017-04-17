import os
import sys

def create_demo_user(username, email, password):
    from django.contrib.auth.models import User
    user = User.objects.create_user(username, email, password)
    user.is_superuser = True
    user.is_staff = True
    user.save()

if __name__ == '__main__':
    sys.path.append(os.path.abspath(os.path.dirname(__file__)).strip('mondja'))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mondja.settings')
    import dotenv
    dotenv.read_dotenv()
    import django
    django.setup()
    create_demo_user('admin', 'admin@example.com', 'admin')
