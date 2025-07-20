from django.http import HttpResponse
from django.shortcuts import render
from django.db import IntegrityError, OperationalError, connection
from datetime import datetime
from .forms import Task4




def task4(request):
    if request.method == 'POST':
        form = Task4(request.POST)
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

                return render(request, 'task4/success.html', {
                    'id': id,
                    'trial': trial,
                    'score': score,
                    'drug': drug,
                })
            
            except OperationalError as ex:
                return HttpResponse(f'Ошибка подключения к БД...<p>{ex}</p>')
            except IntegrityError as ex:
                return HttpResponse(f'Нарушенная целостность данных...<p>{ex}</p>')
            except Exception as ex:
                return HttpResponse(f'Произошла ошибка: <p>{ex}</p>...')
    else:
        form = Task4()
 
    return render(request, 'task4/task4.html', {'form': form})