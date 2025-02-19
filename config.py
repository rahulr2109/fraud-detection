import os
from dotenv import load_dotenv

load_dotenv()

# Kafka
KAFKA_BROKER_URL = os.getenv("KAFKA_BROKER_URL")

# SSL/TLS certificate settings for client certificate authentication
KAFKA_SSL_CAFILE = os.getenv("KAFKA_SSL_CAFILE")
KAFKA_SSL_CERTFILE = os.getenv("KAFKA_SSL_CERTFILE")
KAFKA_SSL_KEYFILE = os.getenv("KAFKA_SSL_KEYFILE")

# MongoDB
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = "fraud_detection"

# Redis
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
