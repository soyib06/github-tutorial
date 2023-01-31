from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from store.bulma_mixin import BulmaMixin

class SignUpForm(BulmaMixin, UserCreationForm):
    first_name = forms.CharField(label='Write first name')
    last_name = forms.CharField(label='Write last name')
    username = forms.CharField(label='Write your Username')
    email = forms.EmailField(label='Write your Email')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'password']



class EditProfileForm(BulmaMixin, forms.ModelForm):
    first_name = forms.CharField(label='Write first name')
    last_name = forms.CharField(label='Write last name')
    username = forms.CharField(label='Write your Username')
    email = forms.EmailField(label='Write your Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name']


class ChangePasswordForm(BulmaMixin, PasswordChangeForm):
    old_password = forms.PasswordInput()
    new1_Password = forms.PasswordInput()
    new2_Password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_possword2']