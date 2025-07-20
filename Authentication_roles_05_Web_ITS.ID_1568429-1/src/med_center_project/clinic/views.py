from django.shortcuts import render
from .models import Doctor
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Doctor
from clinic.serializers import DoctorSerializer, PatientSerializer
from .permissions import IsDoctor


@api_view(['POST'])
def create_doctor_profile(request):
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})

@api_view(['POST'])
def create_patient_profile(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_view(request):
    return Response({
        'message': 'Добро пожаловать в личный кабинет!',
        'user_id': request.user.id,
        'role': request.user.role,
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsDoctor])
def private_account_view(request):
    return Response({'message': 'Доступ только для врачей'})