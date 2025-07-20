from django import forms


class AllData(forms.Form):
    gender = forms.ChoiceField(label='Пол', choices={
        '': '',
        'Мужчина': 'Мужчина', 
        'Женщина': 'Женщина', 
    })
    age = forms.IntegerField(label='Возраст', min_value=0, max_value=120)
    hypertension = forms.BooleanField(label='Есть ли гипертензия?', required=False)
    heart_disease = forms.BooleanField(label='Имеются сердечно-сосудистые заболевания?', required=False)
    ever_married = forms.BooleanField(label='Состояли/-ите в браке?', required=False)
    work_type = forms.ChoiceField(label='Вид работы', choices={
        '': '',
        'Я ребенок': 'Я ребенок',
        'Госслужащий': 'Госслужащий',
        'Никогда не работал': 'Никогда не работал',
        'Негосударственная работа': 'Негосударственная работа',
        'Самозанятый' : 'Самозанятый',
    })
    residence_type = forms.ChoiceField(label='Тип местности проживания', choices={
        '': '',
        'Село': 'Село',
        'Город': 'Город',
    })
    avg_glucose_level = forms.FloatField(label='Средний уровень глюкозы', min_value=0, max_value=999, error_messages={
        '': '',
        'min_value': 'Минимальное значение - 0',
        'max_value': 'Максимальное значение - 999',
    })
    bmi = forms.FloatField(label='Индекс массы тела', min_value=0, max_value=99, error_messages={
        '': '',
        'min_value': 'Минимальное значение - 0',
        'max_value': 'Максимальное значение - 99',
    })
    smoking_status = forms.ChoiceField(label='Статус курения', choices={
        '': '',
        'Ранее курил(а)': 'Ранее курил(а)',
        'Никогда не курил(а)': 'Никогда не курил(а)',
        'Курю': 'Курю',
        'Неизвестно': 'Неизвестно',
    })