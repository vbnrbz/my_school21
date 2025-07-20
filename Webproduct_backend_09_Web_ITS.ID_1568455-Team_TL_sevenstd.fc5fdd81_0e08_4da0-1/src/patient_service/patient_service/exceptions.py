from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

class PatientServiceException(HTTPException):
    """Базовое исключение для сервиса пациента"""
    def __init__(self, detail: str = "Внутренняя ошибка сервиса", status_code: int = 500):
        super().__init__(status_code=status_code, detail=detail)

class PatientNotFoundError(PatientServiceException):
    """Пациент не найден"""
    def __init__(self, patient_uuid: str):
        super().__init__(
            detail=f"Пациент с UUID '{patient_uuid}' не найден",
            status_code=404
        )

class KafkaError(PatientServiceException):
    """Ошибка работы с Kafka"""
    def __init__(self, detail: str = "Ошибка при работе с Kafka"):
        super().__init__(detail=detail, status_code=503)

class MetricsGenerationError(PatientServiceException):
    """Ошибка генерации метрик"""
    def __init__(self, detail: str = "Не удалось сгенерировать метрики"):
        super().__init__(detail=detail, status_code=500)

async def exception_handler(request: Request, exc: PatientServiceException) -> JSONResponse:
    """
    Общий обработчик ошибок сервиса пациента.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.__class__.__name__,
            "detail": exc.detail,
            "path": request.url.path
        }
    )