from django.shortcuts import render
from .forms import ContactForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ContactForm()

    return render(request, 'contacts.html', {'form': form})


def doctors(request):
    return render(request, 'doctors.html')


def services(request):
    return render(request, 'services.html')