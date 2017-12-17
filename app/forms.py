from django import forms
from .models import Memo, Tag


class MemoForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Memo


class TagForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Tag
