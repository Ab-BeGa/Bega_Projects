from django import forms
from .models import Twit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.emai = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Twit
        fields = ('content', 'twitImage')