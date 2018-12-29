import os
import sys


def create_user(username, email, password):
    from django.contrib.auth.models import User
    user = User.objects.create_user(username, email, password)
    user.is_superuser = True
    user.is_staff = True
    user.save()


def create_demo_user():
    root = os.path.abspath(os.path.dirname(__file__)).strip('mondja')
    sys.path.append(root)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mondja.settings')

    import django
    django.setup()
    create_user('admin', 'admin@example.com', 'admin')


def main():
    create_demo_user()


if __name__ == '__main__':
    main()
