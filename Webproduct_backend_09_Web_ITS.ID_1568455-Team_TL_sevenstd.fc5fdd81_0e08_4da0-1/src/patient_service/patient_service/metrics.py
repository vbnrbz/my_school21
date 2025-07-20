import random
import time
import asyncio
from typing import Dict, Union
from config import settings
from kafka import KafkaService
from exceptions import MetricsGenerationError

class MetricsService:
    def __init__(self, patient_uuid: str, use_anomalies: bool = False):
        self.patient_uuid = patient_uuid
        self.use_anomalies = use_anomalies
        self.kafka_service = KafkaService()

    def generate_metrics(self) -> Dict[str, Union[int, float, str]]:

        # Базовые диапазоны для нормальных показателей
        pulse_range = (60, 100)
        resp_rate_range = (12, 20)
        bp_systolic_range = (110, 130)
        bp_diastolic_range = (70, 85)
        spo2_range = (95.0, 99.9)
        temperature_range = (36.0, 37.5)

        if self.use_anomalies:
            # Включаем шанс аномальных данных
            if random.random() < 0.1:  # 10% шанс на аномальный пульс
                pulse_range = (101, 140)  # Тахикардия

            if random.random() < 0.1:
                temperature_range = (38.0, 40.0)  # Высокая температура

            if random.random() < 0.1:
                spo2_range = (80.0, 94.0)  # Низкая сатурация

        return {
            "timestamp": int(time.time()),
            "patient_uuid": self.patient_uuid,
            "pulse": random.randint(*pulse_range),
            "resp_rate": random.randint(*resp_rate_range),
            "bp": f"{random.randint(*bp_systolic_range)}/{random.randint(*bp_diastolic_range)}",
            "spo2": round(random.uniform(*spo2_range), 1),
            "temperature": round(random.uniform(*temperature_range), 1),
        }

    async def send_metrics(self):
        try:
            metrics = self.generate_metrics()
            await self.kafka_service.send_metrics(settings.KAFKA_TOPIC, metrics)
        except Exception as e:
            raise MetricsGenerationError(f"Не удалось отправить метрики: {str(e)}")

    async def start_monitoring(self):
        await self.kafka_service.start()
        try:
            while True:
                await self.send_metrics()
                await asyncio.sleep(settings.METRICS_INTERVAL)
        except asyncio.CancelledError:
            await self.kafka_service.stop()
            raise