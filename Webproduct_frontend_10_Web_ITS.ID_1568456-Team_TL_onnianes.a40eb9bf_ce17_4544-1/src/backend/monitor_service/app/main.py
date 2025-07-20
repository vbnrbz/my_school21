from app.logging import setup_logging

setup_logging()

import uvicorn
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.config import settings
from app.database import init_db
from app.routes import router
import logging
import argparse
from fastapi.middleware.cors import CORSMiddleware

logger = logging.getLogger(__name__)

app = FastAPI(title="Monitor Service")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # для разработки
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем мониторинг сразу после создания app
Instrumentator().instrument(app).expose(app)

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting Monitor Service: initializing DB...")
    await init_db()
    logger.info("Database initialized.")

@app.get("/")
async def root():
    logger.info("Root endpoint called")
    return {"status": "monitor service running"}

@app.get("/patient")
def get_patient_name():
    # Возвращаем имя пациента из состояния приложения (если есть)
    return {"patient_name": getattr(app.state, "patient_name", "unknown")}

def main():
    parser = argparse.ArgumentParser(description="Run Monitor Service with patient name and port")
    parser.add_argument("name", type=str, help="Patient name")
    parser.add_argument("port", type=int, help="Port number")
    args = parser.parse_args()

    app.state.patient_name = args.name
    logger.info(f"Starting Monitor Service for patient '{args.name}' on port {args.port}")

    uvicorn.run("app.main:app", host=settings.HOST, port=args.port, reload=True)

if __name__ == "__main__":
    main()
