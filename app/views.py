"""
Definition of views.
"""

from django.shortcuts import *
from django.http import HttpRequest
from django.template import RequestContext
from django.contrib.auth import models as usermodels
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from app.models import Memo, Tag
from app.forms import MemoForm, TagForm
from mondja.pydenticon_wrapper import create_identicon

@login_required
def home(request):
    """Homeページを表示する．"""
    types = request.GET.get('types')

    if types == 'sort':
        sort_item = request.GET.get('sort_item')
        if sort_item is not '' and request.GET.get('sort_op') == 'desc':
            sort_item = '-' + sort_item

        sort_tag_id = request.GET.get('sort_tag_id')
        all_memo = Memo.objects.all() if sort_tag_id is '' else Tag.objects.get(id = sort_tag_id).memo_set.all()

        sort_user_id = request.GET.get('sort_user_id')
        if sort_user_id is not '':
            all_memo = all_memo.filter(user = usermodels.User.objects.get(id = sort_user_id))

        if sort_item is '':
            all_memo = all_memo.order_by('-pub_date')
        else:
            all_memo = all_memo.order_by(sort_item)

    elif types == 'search':
        search_title = request.GET.get('search_title')
        search_content = request.GET.get('search_content')
        search_tag_id = request.GET.get('search_tag_id')
        search_user_id = request.GET.get('search_user_id')

        if search_tag_id is '':
            all_memo = Memo.objects.all()
        else:
            try:
                all_memo = Tag.objects.get(id = search_tag_id).memo_set.all()
            except ObjectDoesNotExist:
                all_memo = Memo.objects.filter(title = '')

        if search_user_id is not '':
            try:
                user = usermodels.User.objects.get(id = search_user_id)
                all_memo = all_memo.filter(user = user)
            except ObjectDoesNotExist:
                all_memo = Memo.objects.filter(title = '')

        if search_title is not '' and search_content is not '':
            all_memo = all_memo.filter(title__icontains = search_title, content__icontains = search_content)
        elif search_title is not '':
            all_memo = all_memo.filter(title__icontains = search_title)
        elif search_content is not '':
            all_memo = all_memo.filter(content__icontains = search_content)
        else:
            pass

        all_memo = all_memo.order_by('-pub_date')

    elif types == 'tags':
        tids = request.GET.getlist('select_tag')
        if tids == []:
            all_memo = Memo.objects.all().filter(tags__isnull = True)
        else:
            memos = []
            for tid in tids:
                tag = Tag.objects.get(id = tid)
                for memo in tag.memo_set.all():
                    memos.append(memo)
            all_memo = sorted(set(memos), key = lambda x: x.pub_date)
        all_memo.reverse()

    else:
         all_memo = Memo.objects.all().order_by('-pub_date')

    all_memo = all_memo[:100]

    for item in all_memo:
        create_identicon(item.user.username)

    all_users = usermodels.User.objects.annotate(count_memos = Count('memo')).order_by('-count_memos')
    all_tags = Tag.objects.annotate(count_memos = Count('memo')).order_by('-count_memos', '-pub_date')
    top48_tags = all_tags[:48]

    return render(
        request,
        'index.html',
        context_instance = RequestContext(request, locals())
    )

@user_passes_test(lambda u: u.is_superuser)
def add_memo(request):
    """メモを新規に追加する"""
    if request.method == 'POST':
        memo_form = MemoForm(request.POST or None)

        if memo_form.is_valid():
            new_memo = memo_form.save(commit = False)
            new_memo.save()

            tags = request.POST['tags-text']

            for stag in [s.rstrip() for s in tags.split()]:

                if len(Tag.objects.filter(name = stag)) == 0:
                    tag = Tag(name = stag, user = request.user)
                    tag_form = TagForm(instance = tag)

                    if is_valid_tag(stag):
                        new_tag = tag_form.save(commit = False)
                        new_tag.save()
                        new_memo.tags.add(new_tag)
                        new_memo.save()
                else:
                    tag = Tag.objects.get(name = stag)
                    new_memo.tags.add(tag)
                    new_memo.save()

    return HttpResponseRedirect('/#memo')

@user_passes_test(lambda u: u.is_superuser)
def edit_memo(request, id):
    """既存のメモを編集する"""
    memo = Memo.objects.get(id = id)

    if request.method == 'POST' and memo.user == request.user:
        memo_form = MemoForm(request.POST or None, instance = memo)

        if memo_form.is_valid():
            new_memo = memo_form.save(commit = False)
            new_memo.save()
            new_memo.tags.clear()
            new_memo.save()

            tags = request.POST['tags-text']

            for stag in [s.rstrip() for s in tags.split()]:

                if len(Tag.objects.filter(name = stag)) == 0:
                    tag = Tag(name = stag, user = request.user)
                    tag_form = TagForm(instance = tag)

                    if is_valid_tag(stag):
                        new_tag = tag_form.save(commit = False)
                        new_tag.save()
                        new_memo.tags.add(new_tag)
                        new_memo.save()
                else:
                    tag = Tag.objects.get(name = stag)
                    new_memo.tags.add(tag)
                    new_memo.save()

            clear_notused_tag()

    return HttpResponseRedirect('/#memo')

@user_passes_test(lambda u: u.is_superuser)
def delete_memo(request, id):
    """メモを削除する"""
    memo = Memo.objects.get(id = id)

    if request.method == 'POST' and memo.user == request.user:
        memo.delete()

        clear_notused_tag()

    return HttpResponseRedirect('/#memo')

@user_passes_test(lambda u: u.is_superuser)
def refresh_memo(request):
    """メモの表示をリフレッシュする"""
    return HttpResponseRedirect('/#memo')

def is_valid_tag(tag):
    ''' tagの文字長チェック '''
    return len(tag) <= 10

def clear_notused_tag():
    ''' 不要なtagを削除 '''
    for tag in Tag.objects.all():
        if len(tag.memo_set.all()) == 0:
            tag.delete()
