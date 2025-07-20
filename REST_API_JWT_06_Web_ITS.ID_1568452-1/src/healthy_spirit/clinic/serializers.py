from rest_framework import serializers
from .models import Doctor, Patient, Room, Appointment, User
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class DoctorRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    fio = serializers.CharField()
    specialty = serializers.CharField()

    def create(self, validated_data):
        # Создаем пользователя
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_doctor=True
        )
        # Создаем врача и связываем с пользователем
        doctor = Doctor.objects.create(
            user=user,
            fio=validated_data['fio'],
            specialty=validated_data['specialty']
        )
        return doctor

class PatientRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    fio = serializers.CharField()
    birth_date = serializers.DateField()

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_patient=True
        )
        patient = Patient.objects.create(
            user=user,
            fio=validated_data['fio'],
            birth_date=validated_data['birth_date']
        )
        return patient

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class AppointmentCreateSerializer(serializers.Serializer):
    doctor_id = serializers.UUIDField()
    patient_id = serializers.UUIDField()
    room_id = serializers.IntegerField()
    date = serializers.DateTimeField()

class LookupSerializer(serializers.Serializer):
    fio = serializers.CharField()
    specialty = serializers.CharField(required=False)
    birth_date = serializers.DateField(required=False)