from django.http import HttpResponse
from django.shortcuts import render
from .forms import Task1



def task1(request):
    if request.method == 'POST':
        form = Task1(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            trial = form.cleaned_data['trial']
            score = form.cleaned_data['score']
            drug = form.cleaned_data['drug']

            return render(request, 'task1/success.html', {
                'id': id,
                'trial': trial,
                'score': score,
                'drug': drug,
            })
    else:
        form = Task1()
 
    return render(request, 'task1/task1.html', {'form': form})

def index(request):
    return HttpResponse('<h1>Это главная страница</h1>')