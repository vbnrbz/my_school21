import asyncio
import uvicorn
from fastapi import FastAPI, Request
from config import settings
from metrics import MetricsService
from exceptions import exception_handler, PatientNotFoundError, PatientServiceException
import structlog


# Настройка логгирования
def configure_logging():
    structlog.configure(
        processors=[
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ],
        logger_factory=structlog.PrintLoggerFactory(),
        wrapper_class=structlog.BoundLogger,
        cache_logger_on_first_use=True,
    )

configure_logging()
logger = structlog.get_logger()

app = FastAPI(title="Patient Service", version="1.0.0")

# Регистрация общего обработчика исключений
@app.exception_handler(PatientServiceException)
async def handle_patient_service_exception(request: Request, exc: PatientServiceException):
    return await exception_handler(request, exc)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up patient service", patient_uuid=settings.PATIENT_UUID)
    metrics_service = MetricsService(
        patient_uuid=settings.PATIENT_UUID,
        use_anomalies=True
    )
    app.state.monitor_task = asyncio.create_task(metrics_service.start_monitoring())

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down patient service")
    app.state.monitor_task.cancel()
    try:
        await app.state.monitor_task
    except (asyncio.CancelledError, Exception):
        pass

@app.get("/test-error")
async def test_error():
    raise PatientNotFoundError(patient_uuid="non-existent-patient")

@app.get("/")
def read_root():
    return {"service": "patient_service", "status": "running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=settings.DEBUG)