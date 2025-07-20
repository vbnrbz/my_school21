from django.http import HttpResponse
from django.shortcuts import render
from django.db import IntegrityError, OperationalError, connection
from datetime import datetime
from .forms import Task5




def task5(request):
    if request.method == 'POST':
        form = Task5(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            trial = form.cleaned_data['trial']
            score = form.cleaned_data['score']
            drug = form.cleaned_data['drug']
            try:
                with connection.cursor() as cursor:
                    query = f"select trial_id from trials where trial_name = '{trial}';"
                    cursor.execute(query)
                    res = cursor.fetchone()[0]

                    query = 'select max(measurement_id) from measurements'
                    cursor.execute(query)
                    max_m_id = cursor.fetchone()[0]

                    query = f"insert into measurements values ({max_m_id+1}, {id}, {res}, '{datetime.today().date()}', '{drug}', {score});"
                    cursor.execute(query)

                    query = f"select round(AVG(case when drug = '{drug}' and t.trial_name = '{trial}' then condition_score end), 2) from measurements m join trials t on t.trial_id = m.trial_id "
                    cursor.execute(query)
                    res = float(cursor.fetchone()[0])

                normal_res = 'Да' if 0.9 * res <= score <= 1.1 * res else 'Нет'

                return render(request, 'task5/success5.html', {
                    'id': id,
                    'trial': trial,
                    'score': score,
                    'drug': drug,
                    'res': res,
                    'normal_res': normal_res,
                })
            
            except OperationalError as ex:
                return HttpResponse(f'Ошибка подключения к БД...<p>{ex}</p>')
            except IntegrityError as ex:
                return HttpResponse(f'Нарушенная целостность данных...<p>{ex}</p>')
            except Exception as ex:
                return HttpResponse(f'Произошла ошибка: <p>{ex}</p>...')
    else:
        form = Task5()
 
    return render(request, 'task5/task5.html', {'form': form})