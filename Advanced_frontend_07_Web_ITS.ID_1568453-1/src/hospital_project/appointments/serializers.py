import datetime
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import Room, Doctor, Patient, Appointment

User = get_user_model()

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class DoctorRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    fio = serializers.CharField(write_only=True)
    specialty = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'fio', 'specialty')

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        fio = validated_data.pop('fio')
        specialty = validated_data.pop('specialty')
        doctor = Doctor.objects.create(fio=fio, specialty=specialty, available=True)
        user = User.objects.create(username=username, doctor=doctor)
        user.password = make_password(password)
        user.save()
        return user

class PatientRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    fio = serializers.CharField(write_only=True)   
    birth_date = serializers.DateField(write_only=True) 

    class Meta:
        model = User
        fields = ('username', 'password', 'fio', 'birth_date')

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        fio = validated_data.pop('fio')
        birth_date = validated_data.pop('birth_date')
        patient = Patient.objects.create(fio=fio, birth_date=birth_date)
        user = User.objects.create(username=username, patient=patient)
        user.password = make_password(password)
        user.save()
        return user

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'

    def get_age(self, obj):
        if obj.birth_date:
            today = datetime.date.today()
            return today.year - obj.birth_date.year - (
                (today.month, today.day) < (obj.birth_date.month, obj.birth_date.day)
            )
        return None

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    def validate(self, data):
        doctor = data.get('doctor')
        if not doctor:
            raise serializers.ValidationError("Поле doctor обязательно.")
        if not doctor.available:
            raise serializers.ValidationError("Доктор не доступен.")

        patient = data.get('patient')
        if not patient:
            raise serializers.ValidationError("Поле patient обязательно.")

        appointment_date = data.get('date')
        if appointment_date:
            now = datetime.datetime.now(appointment_date.tzinfo)
            next_day_nine = (now + datetime.timedelta(days=1)).replace(hour=9, minute=0, second=0, microsecond=0)
            if appointment_date <= next_day_nine:
                raise serializers.ValidationError("Встреча должна быть после 9:00 утра следующего дня.")
            if appointment_date <= now:
                raise serializers.ValidationError("Встреча не должна быть в прошлом.")
        return data

class CancelAppointmentSerializer(serializers.Serializer):
    appointment_id = serializers.UUIDField()

class PrescriptionSerializer(serializers.Serializer):
    prescriptions = serializers.ListField(
        child=serializers.JSONField(),
        help_text="Список назначений, например: [{'drug': 'B1', 'dosage': '2mg', 'repeat': 'дважды в день'}, ...]"
    )

class PatientLookupSerializer(serializers.Serializer):
    fio = serializers.CharField()
    birth_date = serializers.DateField()

class DoctorLookupSerializer(serializers.Serializer):
    fio = serializers.CharField()
    specialty = serializers.CharField()
