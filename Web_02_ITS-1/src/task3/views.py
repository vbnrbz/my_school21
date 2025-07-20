from django.shortcuts import render
from .forms import Task3



def task3(request):
    if request.method == 'POST':
        form = Task3(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            trial = form.cleaned_data['trial']
            score = form.cleaned_data['score']
            drug = form.cleaned_data['drug']

            return render(request, 'task3/success.html', {
                'id': id,
                'trial': trial,
                'score': score,
                'drug': drug,
            })
    else:
        form = Task3()
 
    return render(request, 'task3/task3.html', {'form': form})