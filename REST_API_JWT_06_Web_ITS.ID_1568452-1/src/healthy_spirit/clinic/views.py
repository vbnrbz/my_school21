from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Doctor, Patient, Room, Appointment
from .serializers import *
from datetime import datetime, timedelta
from drf_spectacular.utils import extend_schema

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class DoctorRegisterView(generics.CreateAPIView):
    serializer_class = DoctorRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doctor = serializer.save()
        return Response({
            'doctor_id': str(doctor.doctor_id),
            'fio': doctor.fio,
            'specialty': doctor.specialty
        }, status=status.HTTP_201_CREATED)

class PatientRegisterView(generics.CreateAPIView):
    serializer_class = PatientRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        patient = serializer.save()
        return Response({
            'patient_id': str(patient.patient_id),
            'fio': patient.fio,
            'birth_date': patient.birth_date
        }, status=status.HTTP_201_CREATED)


@extend_schema(
    request=LookupSerializer,
    responses={'200': {'doctor_id': 'uuid'}}
)
class DoctorLookupView(APIView):
    def get(self, request):
        serializer = LookupSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        doctor = Doctor.objects.filter(
            fio=serializer.validated_data['fio'],
            specialty=serializer.validated_data.get('specialty', '')
        ).first()
        
        if not doctor:
            return Response({'error': 'Doctor not found'}, status=404)
        return Response({'doctor_id': str(doctor.doctor_id)})

@extend_schema(
    request=LookupSerializer,
    responses={'200': {'patient_id': 'uuid'}}
)
class PatientLookupView(APIView):
    def get(self, request):
        serializer = LookupSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        patient = Patient.objects.filter(
            fio=serializer.validated_data['fio'],
            birth_date=serializer.validated_data.get('birth_date')
        ).first()
        
        if not patient:
            return Response({'error': 'Patient not found'}, status=404)
        return Response({'patient_id': str(patient.patient_id)})

@extend_schema(
    request=AppointmentCreateSerializer,
    responses={'201': AppointmentSerializer}
)
class AppointmentCreateView(APIView):
    def post(self, request):
        serializer = AppointmentCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        try:
            date = serializer.validated_data['date']
            if date < datetime.now() + timedelta(days=1):
                return Response(
                    {'error': 'Appointment must be at least 1 day ahead'}, 
                    status=400
                )

            doctor = Doctor.objects.get(
                doctor_id=serializer.validated_data['doctor_id'],
                available=True
            )
            patient = Patient.objects.get(
                patient_id=serializer.validated_data['patient_id']
            )
            room = Room.objects.get(
                room_id=serializer.validated_data['room_id'],
                available=True
            )
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=404
            )

        appointment = Appointment.objects.create(
            doctor=doctor,
            patient=patient,
            room=room,
            date=date
        )
        return Response(
            AppointmentSerializer(appointment).data, 
            status=201
        )

@extend_schema(
    responses={'200': {'status': 'Appointment cancelled'}}
)
class AppointmentCancelView(APIView):
    def patch(self, request, appointment_id):
        try:
            appointment = Appointment.objects.get(appointment_id=appointment_id)
            appointment.cancelled = True
            appointment.save()
            return Response({'status': 'Appointment cancelled'})
        except Appointment.DoesNotExist:
            return Response(
                {'error': 'Appointment not found'}, 
                status=404
            )