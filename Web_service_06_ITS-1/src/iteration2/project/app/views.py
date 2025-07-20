from django.http import HttpResponse
from django.shortcuts import render
from .forms import AllData
import joblib
import numpy as np
from .models import Main
from . import gigachat


# !!!
loaded_model = joblib.load('../model.pkl')

def index(request):
    if request.method == 'POST':
        form = AllData(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            hypertension = form.cleaned_data['hypertension']
            heart_disease = form.cleaned_data['heart_disease']
            ever_married = form.cleaned_data['ever_married']
            work_type = form.cleaned_data['work_type']
            residence_type = form.cleaned_data['residence_type']
            avg_glucose_level = form.cleaned_data['avg_glucose_level']
            bmi = form.cleaned_data['bmi']
            smoking_status = form.cleaned_data['smoking_status']

            # Словари перевода для ИИ
            gender_map = {"Мужчина": 1, "Женщина": 0}
            residence_map = {"Город": 1, "Село": 0}
            work_type_map = {"Я ребенок": 0, "Госслужащий": 1, "Никогда не работал": 2, "Негосударственная работа": 3, "Самозанятый": 4}
            smoking_status_map = {"Ранее курил(а)": 0, "Никогда не курил(а)": 1, "Курю": 2, "Неизвестно": 3}

            patient_data = np.array([[
                gender_map.get(gender),
                age,
                int(hypertension),
                int(heart_disease),
                int(ever_married),
                work_type_map.get(work_type),
                residence_map.get(residence_type),
                avg_glucose_level,
                bmi,
                smoking_status_map.get(smoking_status)
            ]])

            probability = f'{loaded_model.predict_proba(patient_data)[:, 1][0] * 100:.2f}'

            # Словари перевода для SQL
            sql_gender = {'Мужчина': 'Male', 'Женщина': 'Female'}
            sql_residence_type = {'Город': 'Urban', 'Село': 'Rural'}
            sql_work_type = {'Я ребенок': 'children', 'Госслужащий': 'Govt_job', 'Никогда не работал': 'Never_worked', 
                             'Негосударственная работа': 'Private', 'Самозанятый': 'Self-employed'}
            sql_smoking_status = {'Ранее курил(а)': 'formerly smoked', 'Никогда не курил(а)': 'never smoked', 
                                  'Курю': 'smokes', 'Неизвестно': 'Unknown'}

            
            sql = Main(
                gender=sql_gender.get(gender),
                age=age,
                hypertension=int(hypertension),
                heart_disease=int(heart_disease),
                ever_married=ever_married,
                work_type=sql_work_type.get(work_type),
                residence_type=sql_residence_type.get(residence_type),
                avg_glucose_level=avg_glucose_level,
                bmi=bmi,
                smoking_status=sql_smoking_status.get(smoking_status),
                stroke_prediction=probability
            )
            sql.save()
                
            gigachat.connect_gigachat()
            system_text = '''Ты - врач кардиолог. Твоя задача - дать рекомендации на основе анализов, как уменьшить риск инсульта.
            Тебе последовательно передаются следующие данные пациента:
            1) Пол
            2) Возраст
            3) Наличие гипертензии
            4) Наличие сердечно-сосудистых заболеваний
            5) Состояли/-ите в браке
            6) Где работает
            7) Тип местности проживания
            8) Среднее значение глюкозы
            9) Индекс массы тела
            10) Статус курения
            11) Вероятность инсульта
            '''
            user_text = f'''
            1) Пол - {gender}
            2) Возраст - {age}
            3) Наличие гипертензии - {hypertension} 
            4) Наличие сердечно-сосудистых заболеваний - {heart_disease}
            5) Состояли/-ите в браке - {ever_married}
            6) Где работает - {work_type}
            7) Тип местности проживания - {residence_type}
            8) Среднее значение глюкозы - {avg_glucose_level}
            9) Индекс массы тела - {bmi}
            10) Статус курения - {smoking_status}
            11) Вероятность инсульта - {probability}
            '''

            answer = gigachat.ask_gigachat(system_text, user_text)
            

            try:
                return render(request, 'success.html', {
                    'gender': gender,
                    'age': age,
                    'hypertension': 'Да' if hypertension else 'Нет',
                    'heart_disease': 'Да' if heart_disease else 'Нет',
                    'ever_married': 'Да' if ever_married else 'Нет',
                    'work_type': work_type,
                    'residence_type': residence_type,
                    'avg_glucose_level': avg_glucose_level,
                    'bmi': bmi,
                    'smoking_status': smoking_status,
                    'probability': probability,
                    'answer': answer,
                    })
            except Exception as ex:
                return HttpResponse(f'Произошла ошибка: <p>{ex}</p>...')
    else:
        form = AllData()
    return render(request, 'index.html', {'form': form})