"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import Memo, Tag

class MemoForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Memo

class TagForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Tag
