from django.core.exceptions import ValidationError
import re

def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'Password must have at least one uppercase letter, '
            'onde lowercase letter and one number. The lenght '
            'should be at least 8 characters.'
        ),
            code='Invalid'
        )