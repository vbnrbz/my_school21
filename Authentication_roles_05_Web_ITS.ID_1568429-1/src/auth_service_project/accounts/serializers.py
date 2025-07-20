from rest_framework import serializers
from .models import User
import requests


class RegisterDoctorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        requests.post('http://localhost:8000/api/doctor/create/', json={
            'fio': self.context['request'].data.get('fio'),
            'specialty': self.context['request'].data.get('specialty')
        })

        return user
    

class RegisterPatientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        requests.post('http://localhost:8000/api/patient/create/', json={
            'fio': self.context['request'].data.get('fio'),
            'birth_date': self.context['request'].data.get('birth_date')
        })
        
        return user