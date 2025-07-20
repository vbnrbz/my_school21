from django import forms
from django.db import connection


class Task3(forms.Form):
    id = forms.IntegerField(label='Введите ID', min_value=0, error_messages={'min_value': 'Значение должно быть больше и ровно 0!'})
    with connection.cursor() as cursor:
                query = 'select trial_name from trials'
                cursor.execute(query)
                res = cursor.fetchall()
    choices = [(i[0], i[0]) for i in res]
    trial = forms.ChoiceField(label='Выберите исследование', choices=choices)
    score = forms.IntegerField(label='Введите оценку самочувствия (0 - 100)', min_value=0, max_value=100, error_messages={
        'min_value': 'Минимальное значение - 0!',
        'max_value': 'Максимальное значение - 100!',
    })
    drug = forms.ChoiceField(label='Выберите препарат', choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'trial' in self.data:
            with connection.cursor() as cursor:
                t = self.data.get('trial')
                query = f"select med from trials where trial_name = '{t}';"
                cursor.execute(query)
                res = cursor.fetchone()[0]
            self.fields['drug'].choices = [('Плацебо', 'Плацебо'), (res, res)]
