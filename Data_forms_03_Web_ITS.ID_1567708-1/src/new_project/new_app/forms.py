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


# class DoctorForm(forms.ModelForm):
#     class Meta:
#         model = Doctor
#         fields = ['fio', 'birth_date', 'specialty']
#         widgets = {
#             'birth_date': forms.DateInput(attrs={'type': 'date'}),
#         }
#         labels = {
#             'fio': 'ФИО врача',
#             'birth_date': 'Дата рождения',
#             'specialty': 'Специальность',
#         }
    
#     # def clean_fio(self):
#     #     fio = self.cleaned_data.get('fio')
#     #     if not fio:
#     #         raise ValidationError('ФИО врача обязательно для заполнения')
#     #     return fio
    
#     # def clean_specialty(self):
#     #     specialty = self.cleaned_data.get('specialty')
#     #     if not specialty:
#     #         raise ValidationError('Специальность обязательна для заполнения')
#     #     return specialty

    
#     def clean(self):
#         cleaned_data = super().clean()
#         fio = cleaned_data.get('fio')
#         birth_date = cleaned_data.get('birth_date')
#         specialty = cleaned_data.get('specialty')

#         if not fio:
#             raise ValidationError("ФИО врача обязательно для заполнения")
        
#         if not specialty:
#             raise ValidationError("Специальность обязательна для заполнения")

#         if Doctor.objects.filter(fio=fio, birth_date=birth_date).exists():
#             existing_doctor = Doctor.objects.get(fio=fio, birth_date=birth_date)
#             self.add_error(
#                 None,
#                 ValidationError(
#                     f'Врач с такими ФИО и датой рождения уже существует: {existing_doctor.fio} ({existing_doctor.specialty})',
#                     code='duplicate_doctor'
#                 )
#             )
        
#         return cleaned_data


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
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

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