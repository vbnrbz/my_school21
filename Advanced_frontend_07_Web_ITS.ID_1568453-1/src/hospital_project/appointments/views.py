from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
)
from .models import Room, Doctor, Patient, Appointment
from .serializers import (
    RoomSerializer,
    DoctorSerializer,
    PatientSerializer,
    AppointmentSerializer,
    CancelAppointmentSerializer,
    DoctorRegisterSerializer,
    PatientRegisterSerializer,
    PrescriptionSerializer,
    PatientLookupSerializer,
    DoctorLookupSerializer,
)

# -------------------- Эндпойнты для кабинетов (Room) --------------------

@extend_schema(
    summary="Создать кабинет",
    description="Endpoint для создания нового кабинета. Принимает данные: room_name (текст) и available (boolean).",
    request=RoomSerializer,
    responses={201: RoomSerializer}
)
class RoomCreateAPIView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


@extend_schema(
    summary="Список кабинетов",
    description="Endpoint для получения списка всех кабинетов, зарегистрированных в системе.",
    responses={200: RoomSerializer(many=True)}
)
class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

@extend_schema_view(
    get=extend_schema(
        summary="Получить данные кабинета",
        description="Endpoint для получения информации о кабинете по его room_id.",
        responses={200: RoomSerializer}
    ),
    patch=extend_schema(
        summary="Обновить данные кабинета",
        description="Endpoint для обновления информации о кабинете по его room_id. Обновление осуществляется методом PATCH.",
        request=RoomSerializer,
        responses={200: RoomSerializer}
    ),
    delete=extend_schema(
        summary="Удалить кабинет",
        description="Endpoint для удаления кабинета по его room_id.",
        responses={204: {"description": "Кабинет успешно удален."}}
    )
)
class RoomRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'room_id'
    http_method_names = ['get', 'patch', 'delete']


# -------------------- Эндпойнты для врачей --------------------

@extend_schema_view(
    get=extend_schema(
        summary="Получить данные врача",
        description="Endpoint для получения информации о враче по его doctor_id.",
        responses={200: DoctorSerializer}
    ),
    patch=extend_schema(
        summary="Обновить данные врача",
        description="Endpoint для обновления информации о враче по его doctor_id. Обновление осуществляется методом PATCH.",
        request=DoctorSerializer,
        responses={200: DoctorSerializer}
    )
)
class DoctorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'doctor_id'
    http_method_names = ['get', 'patch']


@extend_schema(
    summary="Встречи врача",
    description="Endpoint для получения списка всех встреч, назначенных для врача по его doctor_id.",
    responses={200: AppointmentSerializer(many=True)}
)
class DoctorAppointmentsAPIView(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        doctor_id = self.kwargs.get('doctor_id')
        return Appointment.objects.filter(doctor__doctor_id=doctor_id)


@extend_schema(
    summary="Список всех врачей",
    description="Возвращает список всех врачей, зарегистрированных в системе.",
    responses={200: DoctorSerializer(many=True)}
)
class DoctorListAPIView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


# -------------------- Эндпойнты для пациентов --------------------

@extend_schema_view(
    get=extend_schema(
        summary="Получить данные пациента",
        description="Endpoint для получения информации о пациенте по его patient_id.",
        responses={200: PatientSerializer}
    ),
    patch=extend_schema(
        summary="Обновить данные пациента",
        description="Endpoint для обновления информации о пациенте по его patient_id. Обновление осуществляется методом PATCH.",
        request=PatientSerializer,
        responses={200: PatientSerializer}
    )
)
class PatientRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'patient_id'
    http_method_names = ['get', 'patch']


@extend_schema(
    summary="Добавить назначения пациенту",
    description="Endpoint для добавления или обновления назначений для пациента. Принимает JSON с полем prescriptions, содержащим массив объектов.",
    request=PrescriptionSerializer,
    responses={200: {"description": "Назначения успешно обновлены."}}
)
class PatientAddPrescriptionsAPIView(APIView):
    serializer_class = PrescriptionSerializer

    def post(self, request, patient_id):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            patient = get_object_or_404(Patient, patient_id=patient_id)
            patient.prescriptions = serializer.validated_data['prescriptions']
            patient.save()
            return Response({"message": "Назначения успешно обновлены."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    summary="Список всех пациентов",
    description="Возвращает список всех пациентов, зарегистрированных в системе.",
    responses={200: PatientSerializer(many=True)}
)
class PatientListAPIView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


# -------------------- Эндпойнты для встреч (Appointment) --------------------

@extend_schema(
    summary="Создать встречу",
    description="Endpoint для создания новой встречи. Принимает doctor (UUID), patient (UUID), room (ID) и date (DateTime). "
                "Проверяет, что доктор существует и доступен, пациент существует, а дата соответствует требованиям (встреча должна быть после 9:00 утра следующего дня).",
    request=AppointmentSerializer,
    responses={201: AppointmentSerializer}
)
class AppointmentCreateAPIView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


@extend_schema(
    summary="Отменить встречу",
    description="Endpoint для отмены встречи. Принимает appointment_id (UUID) и устанавливает поле cancelled в true.",
    request=CancelAppointmentSerializer,
    responses={200: {"description": "Встреча успешно отменена."}}
)
class CancelAppointmentAPIView(APIView):
    serializer_class = CancelAppointmentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            appointment_id = serializer.validated_data['appointment_id']
            try:
                appointment = Appointment.objects.get(appointment_id=appointment_id)
            except Appointment.DoesNotExist:
                return Response({"error": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)
            appointment.cancelled = True
            appointment.save()
            return Response({"message": "Встреча успешно отменена."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------- Эндпойнты для регистрации --------------------

@extend_schema(
    summary="Регистрация врача",
    description="Endpoint для регистрации нового пользователя с ролью врача. Создаёт объект Doctor с полями fio и specialty, "
                "а затем связывает его с пользователем.",
    request=DoctorRegisterSerializer,
    responses={201: DoctorRegisterSerializer}
)
class DoctorRegisterAPIView(generics.CreateAPIView):
    serializer_class = DoctorRegisterSerializer


@extend_schema(
    summary="Регистрация пациента",
    description="Endpoint для регистрации нового пользователя с ролью пациента. Создаёт объект Patient с полями fio и birth_date, "
                "а затем связывает его с пользователем. Возраст вычисляется автоматически при сохранении.",
    request=PatientRegisterSerializer,
    responses={201: PatientRegisterSerializer}
)
class PatientRegisterAPIView(generics.CreateAPIView):
    serializer_class = PatientRegisterSerializer


# -------------------- Новые эндпойнты для поиска UUID по параметрам --------------------

@extend_schema(
    summary="Получить UUID пациента по ФИО и дате рождения",
    description="Возвращает UUID пациента, если найдена запись с указанными ФИО и датой рождения.",
    parameters=[
        OpenApiParameter(name="fio", type=str, description="ФИО пациента"),
        OpenApiParameter(name="birth_date", type=str, description="Дата рождения пациента в формате YYYY-MM-DD"),
    ],
    responses={200: {"description": "Patient UUID", "content": {"application/json": {"example": {"patient_id": "123e4567-e89b-12d3-a456-426614174000"}}}}}
)
class PatientUUIDLookupAPIView(APIView):
    def get(self, request):
        serializer = PatientLookupSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        fio = serializer.validated_data['fio']
        birth_date = serializer.validated_data['birth_date']
        try:
            patient = Patient.objects.get(fio=fio, birth_date=birth_date)
        except Patient.DoesNotExist:
            return Response({"error": "Пациент не найден."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"patient_id": str(patient.patient_id)})


@extend_schema(
    summary="Получить UUID врача по ФИО и специальности",
    description="Возвращает UUID врача, если найдена запись с указанными ФИО и специальностью.",
    parameters=[
        OpenApiParameter(name="fio", type=str, description="ФИО врача"),
        OpenApiParameter(name="specialty", type=str, description="Специальность врача"),
    ],
    responses={200: {"description": "Doctor UUID", "content": {"application/json": {"example": {"doctor_id": "123e4567-e89b-12d3-a456-426614174000"}}}}}
)
class DoctorUUIDLookupAPIView(APIView):
    def get(self, request):
        serializer = DoctorLookupSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        fio = serializer.validated_data['fio']
        specialty = serializer.validated_data['specialty']
        try:
            doctor = Doctor.objects.get(fio=fio, specialty=specialty)
        except Doctor.DoesNotExist:
            return Response({"error": "Доктор не найден."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"doctor_id": str(doctor.doctor_id)})
