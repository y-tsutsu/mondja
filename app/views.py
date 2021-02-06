from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from pure_pagination import PageNotAnInteger, Paginator

from .forms import MemoForm, TagForm
from .models import Memo, Tag


@login_required
def home(request):
    ''' Homeページを表示する． '''
    types = request.GET.get('types')

    if types == 'sort':
        sort_item = request.GET.get('sort_item')
        if sort_item != '' and request.GET.get('sort_op') == 'desc':
            sort_item = '-' + sort_item

        sort_tag_id = request.GET.get('sort_tag_id')
        all_memo = Memo.objects.all() if sort_tag_id == '' else Tag.objects.get(id=sort_tag_id).memo_set.all()

        sort_user_id = request.GET.get('sort_user_id')
        if sort_user_id != '':
            all_memo = all_memo.filter(user=User.objects.get(id=sort_user_id))

        if sort_item == '':
            all_memo = all_memo.order_by('-pub_date')
        else:
            all_memo = all_memo.order_by(sort_item)

    elif types == 'search':
        search_title = request.GET.get('search_title')
        search_content = request.GET.get('search_content')
        search_tag_id = request.GET.get('search_tag_id')
        search_user_id = request.GET.get('search_user_id')

        all_memo = Memo.objects.all() if search_tag_id == '' else Tag.objects.get(id=search_tag_id).memo_set.all()

        if search_user_id != '':
            user = User.objects.get(id=search_user_id)
            all_memo = all_memo.filter(user=user)

        if search_title != '' and search_content != '':
            all_memo = all_memo.filter(title__icontains=search_title, content__icontains=search_content)
        elif search_title != '':
            all_memo = all_memo.filter(title__icontains=search_title)
        elif search_content != '':
            all_memo = all_memo.filter(content__icontains=search_content)
        else:
            pass

        all_memo = all_memo.order_by('-pub_date')

    elif types == 'tags':
        tids = request.GET.getlist('select_tag')
        if tids == []:
            all_memo = Memo.objects.all().filter(tags__isnull=True).order_by('-pub_date')
        else:
            memos = set()
            for tid in tids:
                try:
                    tag = Tag.objects.get(id=tid)
                    for memo in tag.memo_set.all():
                        memos.add(memo)
                except ObjectDoesNotExist:
                    pass    # タグ検索している状態でdeleteしたあとのredirectでこのpathをとおる可能性あり
            all_memo = sorted(memos, key=lambda x: x.pub_date, reverse=True)

    else:
        all_memo = Memo.objects.all().order_by('-pub_date')

    paginator = Paginator(all_memo, 30, request=request)
    page = request.GET.get('page', 1)

    try:
        all_memo = paginator.page(page)
    except PageNotAnInteger:
        all_memo = paginator.page(1)

    all_users = User.objects.annotate(count_memos=Count('memo')).order_by('-count_memos')
    all_tags = Tag.objects.annotate(count_memos=Count('memo')).order_by('-count_memos', '-pub_date')
    top_tags = all_tags[:72]
    now_str = '{0:%Y-%m-%d %H:%M:%S}'.format(timezone.now().astimezone(timezone.get_default_timezone()))

    return render(request, 'app/index.html', locals())


@user_passes_test(lambda u: u.is_superuser, login_url=settings.LOGIN_URL + '?need_superuser=True')
def add_memo(request):
    ''' メモを新規に追加する． '''
    if request.method == 'POST':
        memo_form = MemoForm(request.POST or None)
        add_or_edit_memo(request, memo_form, False)

    if 'HTTP_REFERER' in request.META:
        return redirect(request.META['HTTP_REFERER'] + '#memo')
    return redirect('/#memo')


@user_passes_test(lambda u: u.is_superuser, login_url=settings.LOGIN_URL + '?need_superuser=True')
def edit_memo(request, id):
    ''' 既存のメモを編集する． '''
    memo = get_object_or_404(Memo, pk=id)

    if request.method == 'POST':
        if memo.user != request.user:
            raise PermissionDenied

        memo_form = MemoForm(request.POST or None, instance=memo)
        add_or_edit_memo(request, memo_form, True)

    if 'HTTP_REFERER' in request.META:
        return redirect(request.META['HTTP_REFERER'] + '#memo')
    return redirect('/#memo')


def add_or_edit_memo(request, memo_form, is_edit):
    ''' メモを新規に追加，または既存のメモを編集する． '''
    if memo_form.is_valid():
        new_memo = memo_form.save(commit=False)
        new_memo.save()
        if is_edit:
            new_memo.tags.clear()
            new_memo.save()

        tags = request.POST['tags-text']

        for stag in [s.rstrip() for s in tags.split()]:
            if len(Tag.objects.filter(name=stag)) == 0:
                tag = Tag(name=stag, user=request.user)
                tag_form = TagForm(instance=tag)

                if is_valid_tag(stag):
                    new_tag = tag_form.save(commit=False)
                    new_tag.save()
                    new_memo.tags.add(new_tag)
                    new_memo.save()
                else:
                    messages.error(request, 'Incorrect tag name. ({0})'.format(stag))
            else:
                tag = get_object_or_404(Tag, name=stag)
                new_memo.tags.add(tag)
                new_memo.save()

        if is_edit:
            clear_notused_tags()
    else:
        messages.error(request, 'Incorrect title or content.')


@user_passes_test(lambda u: u.is_superuser, login_url=settings.LOGIN_URL + '?need_superuser=True')
def delete_memo(request, id):
    ''' メモを削除する． '''
    memo = get_object_or_404(Memo, pk=id)

    if request.method == 'POST':
        if memo.user != request.user:
            raise PermissionDenied

        memo.delete()
        clear_notused_tags()

    if 'HTTP_REFERER' in request.META:
        return redirect(request.META['HTTP_REFERER'] + '#memo')
    return redirect('/#memo')


@user_passes_test(lambda u: u.is_superuser, login_url=settings.LOGIN_URL + '?need_superuser=True')
def refresh_memo(request):
    ''' メモの表示をリフレッシュする． '''
    return redirect('/#memo')


def is_valid_tag(tag):
    ''' tagの文字長チェック '''
    return len(tag) <= 10


def clear_notused_tags():
    ''' 不要なtagを削除 '''
    for tag in Tag.objects.all():
        if len(tag.memo_set.all()) == 0:
            tag.delete()
