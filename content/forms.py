from django import forms
from .models import Progress, News


class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['name', 'progress']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']