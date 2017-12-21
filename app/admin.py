from django.contrib import admin

from .models import Memo, Tag


class MemoAdmin(admin.ModelAdmin):
    filter_horizontal = ['tags']


admin.site.register(Memo, MemoAdmin)
admin.site.register(Tag)
