from django import forms
from django.contrib.auth.models import User
from .models import Progress, News


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Repeat password')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['name', 'progress']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']