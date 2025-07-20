from django.urls import path
from .views import register_doctor, register_patient, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/doctor/', register_doctor, name='register_doctor'),
    path('register/patient/', register_patient, name='register_patient'),
]