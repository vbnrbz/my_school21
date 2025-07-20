from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, DoctorForm
from .models import Room, Doctor
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect, HttpResponseServerError, HttpResponse
from django.core.paginator import Paginator
import csv
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db import IntegrityError
from datetime import datetime
from django.core.exceptions import ValidationError

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
    
    fio_filter = request.GET.get('fio')
    specialty_filter = request.GET.get('specialty')
    available_filter = request.GET.get('available')

    if fio_filter:
        doctors_list = doctors_list.filter(fio__icontains=fio_filter)
    if specialty_filter:
        doctors_list = doctors_list.filter(specialty__icontains=specialty_filter)
    if available_filter:
        doctors_list = doctors_list.filter(available=(available_filter == 'true'))

    sort = request.GET.get('sort')
    if sort:
        doctors_list = doctors_list.order_by(sort)

    per_page = request.GET.get('per_page', 5)
    paginator = Paginator(doctors_list, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
        
    return render(request, 'doctors.html', {
        'page_obj': page_obj,
        'per_page': per_page,
    })


def services(request):
    return render(request, 'services.html')


def room_list(request):
    try:
        rooms = Room.objects.all().order_by('room_id')
        return render(request, 'rooms.html', {'rooms': rooms})
    except Exception as e:
        return HttpResponseServerError('Произошла ошибка при загрузке списка кабинетов')


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
    
    if request.method == 'GET':
        storage = messages.get_messages(request)
        for message in storage:
            pass
    
    return render(request, 'add_doctor.html', {
        'form': form,
        'show_duplicates': hasattr(form, 'duplicates')
    })


def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, doctor_id=doctor_id)
    if request.method == 'POST':
        if 'delete' in request.POST:
            doctor.delete()
            messages.success(request, 'Врач успешно удален!')
            return redirect('doctors')
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные врача успешно обновлены!')
            return redirect('doctors')
    else:
        form = DoctorForm(instance=doctor)

    return render(request, 'doctor_edit.html', {'form': form})


def doctor_info(request, doc_id):
    try:
        doctor = Doctor.objects.get(doctor_id=doc_id)
    except Doctor.DoesNotExist:
        raise Http404("Врач не найден")
    return render(request, 'doctor_info.html', {'doctor': doctor})


def export_doctors_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="doctors.csv"'

    writer = csv.writer(response)
    writer.writerow(['doctor_id', 'fio', 'birth_date', 'available', 'specialty'])

    doctors = Doctor.objects.all().values_list('doctor_id', 'fio', 'birth_date', 'available', 'specialty')
    for doctor in doctors:
        writer.writerow(doctor)

    return response


def export_doctors_json(request):
    doctors = Doctor.objects.all().values('doctor_id', 'fio', 'birth_date', 'available', 'specialty')
    data = list(doctors)

    response = HttpResponse(json.dumps(data, indent=2, ensure_ascii=False, cls=DjangoJSONEncoder), content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="doctors.json"'
    return response


def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValidationError(f'Неверная дата: {date_str}')

def import_doctors(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_format = request.POST['format']
        success_count = 0
        skipped_count = 0
        
        try:
            if file_format == 'csv':
                decoded_file = file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(decoded_file)
                
                for row in reader:
                    try:
                        birth_date = validate_date(row['birth_date'])
                        
                        Doctor.objects.create(
                            doctor_id=row['doctor_id'],
                            fio=row['fio'],
                            birth_date=row['birth_date'],
                            available=row['available'] == 'True',
                            specialty=row['specialty']
                        )
                        success_count += 1
                    except IntegrityError:
                        skipped_count += 1
                        continue
                
            elif file_format == 'json':
                data = json.loads(file.read().decode('utf-8'))
                
                for item in data:
                    try:
                        Doctor.objects.create(
                            doctor_id=item['doctor_id'],
                            fio=item['fio'],
                            birth_date=item['birth_date'],
                            available=item['available'],
                            specialty=item['specialty']
                        )
                        success_count += 1
                    except IntegrityError:
                        skipped_count += 1
                        continue
            
            messages.success(request, f'Успешно импортировано: {success_count}, пропущено дубликатов: {skipped_count}')
            return redirect('doctors')
            
        except Exception as e:
            messages.error(request, f'Ошибка при импорте: {str(e)}')
            return redirect('import_doctors')
    
    return render(request, 'doctors_import.html')