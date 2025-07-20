from aiokafka import AIOKafkaConsumer
from app.config import settings
from app.data import DataService
import asyncio
import json
import logging

logger = logging.getLogger(__name__)

class KafkaService:
    def __init__(self):
        self.consumer = AIOKafkaConsumer(
            settings.kafka_topic,
            bootstrap_servers=settings.kafka_bootstrap_servers,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        )

    async def start(self):
        await self.consumer.start()
        logger.info("Kafka consumer started")

    async def stop(self):
        await self.consumer.stop()
        logger.info("Kafka consumer stopped")

    async def process_messages(self):
        try:
            async for msg in self.consumer:
                logger.info(f"Received message: {msg.value}")
                await DataService.save_patient_data(msg.value)
        except Exception as e:
            logger.error(f"Error while processing Kafka message: {e}")
