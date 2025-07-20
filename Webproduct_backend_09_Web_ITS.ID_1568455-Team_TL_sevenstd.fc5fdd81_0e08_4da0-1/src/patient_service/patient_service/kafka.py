from aiokafka import AIOKafkaProducer
from typing import Optional
from config import settings
import json
import structlog

logger = structlog.get_logger()

class KafkaService:
    def __init__(self):
        self.bootstrap_servers = settings.KAFKA_BOOTSTRAP_SERVERS
        self.producer: Optional[AIOKafkaProducer] = None

    async def start(self):
        """Инициализирует Kafka Producer."""
        logger.info("Запуск Kafka Producer", servers=self.bootstrap_servers)
        try:
            self.producer = AIOKafkaProducer(
                bootstrap_servers=self.bootstrap_servers,
                enable_idempotence=True  # Гарантия доставки без дубликатов
            )
            await self.producer.start()
        except Exception as e:
            logger.error("Ошибка при запуске Kafka Producer", error=str(e))
            raise

    async def stop(self):
        """Останавливает Kafka Producer."""
        if self.producer:
            logger.info("Остановка Kafka Producer")
            await self.producer.stop()

    async def send_metrics(self, topic: str, metrics: dict):
        """
        Отправляет метрики в указанный топик Kafka.

        """
        try:
            await self.producer.send(topic, json.dumps(metrics).encode("utf-8"))
            logger.info("Метрики отправлены в Kafka", topic=topic, metrics=metrics)
        except Exception as e:
            logger.error("Ошибка при отправке метрик в Kafka", error=str(e))