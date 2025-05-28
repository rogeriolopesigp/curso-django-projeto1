from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import strong_password




class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(
        required = True,
        label= 'Password2',
        widget = forms.PasswordInput(attrs={
                'placeholder': 'Repeat your password'
            }),
        error_messages ={
            'required': 'Password must not be empty.'
        },
        validators=[strong_password]
    )

    first_name = forms.CharField(
        error_messages={'required': 'This field must not be empty.'},
        required = True,
        label='First name',
        widget = forms.TextInput(attrs={
                'placeholder': 'Type your first name here'
            }),
    )
    last_name = forms.CharField(
        error_messages={'required': 'This field must not be empty.'},
        required = True,
        label='Last name',
        widget = forms.TextInput(attrs={
                'placeholder': 'Type your last name here'
            }),
    )

    username = forms.CharField(
        required = True,
        error_messages ={
            'required': 'This field must not be empty.',
            'min_length': 'Username must have at least 4 characters',
            'max_length': 'Username must have max 150 characters'
            },
        min_length=4, 
        max_length=150,
        help_text = 'Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.',
        label='Username',
        widget = forms.TextInput(attrs={
                'placeholder': 'Type your username here'
            }),
    )

    email = forms.CharField(
        error_messages={'required': 'This field must not be empty.'},
        required = True,
        help_text = 'The e-mail must be valid.',
        label='E-mail',
        widget = forms.TextInput(attrs={
                'placeholder': 'Type your e-mail here'
            }),
    )


    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'username': 'Username',
            'email': 'E-mail',
            'password': 'Password',
        }

        help_texts = {
            'password': 'Password must have at least one uppercase letter, '
                        'onde lowercase letter and one number. The lenght '
                        'should be at least 8 characters.',
        }

        error_messages = {
            'password': {
                'required': 'This field must not be empty.'
            }
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Type your first name here'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Type your last name here'
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'Type your username here'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Type your e-mail here'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Type your password here'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise ValidationError('User e-mail is already in use', code='invalid')
        return email          

    def clean_password(self):
        data = self.cleaned_data.get('password')

        if 'atenção' in data:
            raise ValidationError(
                'Não digite %(valor)s no campo password',
                code='invalid',
                params={ 'valor': '"atenção"'}
            )

        return data

    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')

        if 'John' in data:
            raise ValidationError(
                'Não digite %(valor)s no campo first name',
                code='invalid',
                params={ 'valor': '"John"'}
            )

        return data
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise ValidationError({
                'password': 'Password and password2 must be equal'
            })