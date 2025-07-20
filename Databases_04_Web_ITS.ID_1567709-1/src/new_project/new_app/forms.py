from django import forms
from .models import Doctor
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ваше имя',
        }),
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Ваше email',
        }),
    )

    message = forms.CharField(
        label='Сообщение',
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Ваше сообщение',
            'rows': 3,
        }),
    )
    

class DoctorForm(forms.ModelForm):
    confirm_duplicate = forms.BooleanField(
        required=False,
        widget=forms.HiddenInput(),
        initial=False
    )

    class Meta:
        model = Doctor
        fields = ['fio', 'birth_date', 'specialty']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth_date'].input_formats = ['%Y-%m-%d', '%d.%m.%Y']

    def clean(self):
        cleaned_data = super().clean()
        fio = cleaned_data.get('fio')
        birth_date = cleaned_data.get('birth_date')
        confirm = cleaned_data.get('confirm_duplicate')

        if not confirm and fio and birth_date:
            duplicates = Doctor.objects.filter(fio=fio, birth_date=birth_date)
            if duplicates.exists():
                self.duplicates = duplicates
                raise ValidationError(
                    "Врач с такими ФИО и датой рождения уже существует. "
                    "Подтвердите добавление, если это другой врач."
                )
        return cleaned_data