from django import forms


class Task1(forms.Form):
    id = forms.IntegerField(label='Введите ID', min_value=0, error_messages={'min_value': 'Значение должно быть больше и ровно 0!'})
    trial = forms.ChoiceField(label='Выберите исследование', choices=[('Иссл1', 'Иссл1'), ('Иссл2', 'Иссл2')])
    score = forms.IntegerField(label='Введите оценку самочувствия (0 - 100)', min_value=0, max_value=100, error_messages={
        'min_value': 'Минимальное значение - 0!',
        'max_value': 'Максимальное значение - 100!',
    })
    drug = forms.ChoiceField(label='Выберите препарат', choices=[('Плацебо', 'Плацебо'), ('Препарат1', 'Препарат1')])