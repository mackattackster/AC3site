from django import forms

class PasswordForm(forms.Form):
    nPassword = forms.CharField(widget=forms.PasswordInput)
    cPassword = forms.CharField(widget=forms.PasswordInput)