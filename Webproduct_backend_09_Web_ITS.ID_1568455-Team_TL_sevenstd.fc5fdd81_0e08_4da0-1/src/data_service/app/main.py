from app.logging import setup_logging

setup_logging()

import asyncio
from fastapi import FastAPI
from app.database import init_db
from app.kafka import KafkaService
import logging
import argparse
import uvicorn

logger = logging.getLogger(__name__)

app = FastAPI()

kafka_service = None  # переменная для KafkaService

@app.on_event("startup")
async def startup_event():
    global kafka_service
    logger.info("Initializing DB and starting Kafka consumer...")
    await init_db()
    kafka_service = KafkaService()  # создаём внутри async функции, чтобы был доступ к event loop
    await kafka_service.start()
    asyncio.create_task(kafka_service.process_messages())

@app.on_event("shutdown")
async def shutdown_event():
    global kafka_service
    if kafka_service:
        logger.info("Shutting down Kafka consumer...")
        await kafka_service.stop()

@app.get("/")
def read_root():
    return {"status": "running"}

# Пример эндпоинта, чтобы проверить, что name передаётся
@app.get("/patient")
def get_patient_name():
    return {"patient_name": app.state.patient_name}

def main():
    parser = argparse.ArgumentParser(description="Run FastAPI app with patient name and port")
    parser.add_argument("name", type=str, help="Patient name")
    parser.add_argument("port", type=int, help="Port number to run on")
    args = parser.parse_args()

    # Сохраняем имя пациента в app.state для доступа из роутов
    app.state.patient_name = args.name
    logger.info(f"Starting app for patient '{args.name}' on port {args.port}")

    uvicorn.run("app.main:app", host="0.0.0.0", port=args.port, reload=True)

if __name__ == "__main__":
    main()
