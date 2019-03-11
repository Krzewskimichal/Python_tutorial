from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Login', max_length=128)
    password = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Login', max_length=128)
    password1 = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', max_length=128, widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', max_length=256)
