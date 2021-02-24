from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from .models import Profile


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Username or email',
        widget=forms.TextInput(attrs={'autofocus': True})
    )


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']):
            raise forms.ValidationError('A user with this email address is already registered.')
        return cd['email']

    class Meta:
        model = User
        fields = ('username', 'email')


class UserEditForm(forms.ModelForm):

    def clean_email(self):
        cd = self.cleaned_data
        if self.has_changed() and User.objects.filter(email=cd['email']):
            raise forms.ValidationError('A user with this email address is already registered.')
        return cd['email']

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
