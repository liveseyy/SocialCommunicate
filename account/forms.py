from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']):
            raise forms.ValidationError('A user with this email address is already registered')
        return cd['email']

    class Meta:
        model = User
        fields = ('username', 'email')
