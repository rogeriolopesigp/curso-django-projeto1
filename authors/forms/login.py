from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(attrs={
                'placeholder': 'Type your username'
            }),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
                'placeholder': 'Type your password'
            }),
    )
