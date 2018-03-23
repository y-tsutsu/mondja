from django import forms

from .models import Memo, Tag


class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = '__all__'


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
