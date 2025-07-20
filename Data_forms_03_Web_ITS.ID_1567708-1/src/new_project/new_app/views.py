from django.shortcuts import render, redirect
from .forms import ContactForm, DoctorForm
from .models import Room, Doctor
from django.contrib import messages
from django.http import Http404, HttpResponseServerError
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError


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
    doctors_list = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors_list})


def services(request):
    return render(request, 'services.html')


def room_list(request):
    try:
        rooms = Room.objects.all().order_by('room_id')
        return render(request, 'rooms.html', {'rooms': rooms})
    except Exception as e:
        return HttpResponseServerError('Произошла ошибка при загрузке списка кабинетов')


# def create_doctor(request):
#     try:
#         if request.method == 'POST':
#             form = DoctorForm(request.POST)
#             if form.is_valid():
#                 try:
#                     form.save()
#                     messages.success(request, 'Врач успешно добавлен!')
#                     return redirect('doctors')
#                 except IntegrityError:
#                     messages.error(request, 'Произошла ошибка при сохранении врача')
#             else:
#                 messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
#         else:
#             form = DoctorForm()
        
#         return render(request, 'add_doctor.html', {'form': form})
#     except Exception as e:
#         return HttpResponseServerError('Произошла ошибка при обработке формы')

def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        
        if 'confirm_duplicate' in request.POST:
            form = DoctorForm(request.POST)
            form.data = form.data.copy()
            form.data['confirm_duplicate'] = True
            
        if form.is_valid():
            form.save()
            messages.success(request, 'Врач успешно добавлен!')
            return redirect('doctors')
    else:
        form = DoctorForm()
    
    return render(request, 'add_doctor.html', {
        'form': form,
        'show_duplicates': hasattr(form, 'duplicates')
    })