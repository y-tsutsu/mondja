def set_superuser(user, *args, **kwargs):
    ''' ソーシャルログインで作成されたユーザをスーパーユーザに設定します． '''
    user.is_superuser = True
    user.save()
