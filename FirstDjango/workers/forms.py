from django import forms
from django.forms.widgets import NumberInput

from workers.models import Worker


class WorkerCreateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'salary', 'note', 'photo']

        labels = {
            'name': "Ім'я робітника:",
            'salary': 'Заробітня плата',
            'note': 'Примітки',
            'photo': 'Особисте фото'
        }

        # help_texts = {
        #     'name': "Введіть ім'я:"
        # }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': "Введіть ім'я:",
                'class': 'form-control'
            }),
            'salary': forms.NumberInput(attrs={
                'min': '0',
                'class': 'form-control',
                'step': '0.1'
            }),
            'note': forms.Textarea(attrs={
                'placeholder': 'Введіть примітку',
                'class': 'form-control',
                'rows': 5
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'accept': 'image/*'
            })
        }

    # валідатор тут


class WorkerSearchForm(forms.Form):
    name = forms.CharField(
        label="Ім'я робітника",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': "Ім'я:",
            'class': 'form-control'
        })
    )

    min_salary = forms.DecimalField(
        label='Мінімальна зарплата',
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Від:',
            'class': 'form-control'
        })
    )

    max_salary = forms.DecimalField(
        label='Максимальна зарплата',
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'До:',
            'class': 'form-control'
        })
    )
