from django import forms
from recipes.models import Recipe
from django.core.exceptions import ValidationError
from collections import defaultdict
from utils.strings import is_positive_number

class AuthorRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)

    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'preparation_time',
            'preparation_time_unit',
            'servings',
            'servings_unit',
            'preparation_steps',
            'cover',
        ]
        widgets = {
            'cover': forms.FileInput(
                attrs={
                    'class': 'span-2'
                }
            ),
            'preparation_steps': forms.Textarea(
                attrs={
                    'class': 'span-2'
                }
            ),
            'servings_unit': forms.Select(
                choices=(
                    ('Porções', 'Porções'),
                    ('Pessoas', 'Pessoas'),
                    ('Fatias', 'Fatias'),
                )
            ),
            'preparation_time_unit': forms.Select(
                choices=(
                    ('Horas', 'Horas'),
                    ('Minutos', 'Minutos'),
                )
            ),
        }

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')

        if len(title) < 5:
            self._my_errors['title'].append('Title must have at least 5 chars.')
        if title == description:
            self._my_errors['title'].append('Title cannot be equal to description.')
            self._my_errors['description'].append('Description cannot be equal to title.')

        if self._my_errors:
            raise ValidationError(self._my_errors)        

        return super_clean
    
    def clean_preparation_time(self):
        field_value = self.cleaned_data.get('preparation_time')

        if not is_positive_number(field_value):
            self._my_errors['preparation_time'].append('Must be a positive number.')

        return field_value
    
    def clean_servings(self):
        field_value = self.cleaned_data.get('servings')

        if not is_positive_number(field_value):
            self._my_errors['servings'].append('Must be a positive number.')

        return field_value