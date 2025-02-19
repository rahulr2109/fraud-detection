from kafka import KafkaProducer, KafkaConsumer
import json
from config import KAFKA_BROKER_URL, KAFKA_SSL_CAFILE, KAFKA_SSL_CERTFILE, KAFKA_SSL_KEYFILE

class KafkaService:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=[KAFKA_BROKER_URL],  # Must be a list
            security_protocol="SSL",
            ssl_cafile=KAFKA_SSL_CAFILE,
            ssl_certfile=KAFKA_SSL_CERTFILE,
            ssl_keyfile=KAFKA_SSL_KEYFILE,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )

    def send_message(self, topic, message):
        future = self.producer.send(topic, value=message)
        result = future.get(timeout=60)  # Wait for the send to complete
        print(f"Sent message to topic {topic}: {result}") # Print the message details
        self.producer.flush()   # Force any buffered messages to be sent



    def consume_messages(self, topic, callback):
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=[KAFKA_BROKER_URL],
            security_protocol="SSL",
            ssl_cafile=KAFKA_SSL_CAFILE,
            ssl_certfile=KAFKA_SSL_CERTFILE,
            ssl_keyfile=KAFKA_SSL_KEYFILE,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id="fraud-detection-group"
        )
        for message in consumer:
            callback(message.value)
            print(f"Consumed message from topic {topic}")

kafka_service = KafkaService()
