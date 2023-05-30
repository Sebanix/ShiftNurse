from django import forms


class LoginForm(forms.Form):
    rut = forms.CharField(max_length=8, required=True)
    dv = forms.CharField(max_length=1, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
