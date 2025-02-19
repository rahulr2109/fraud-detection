from services.kafka_service import kafka_service
from services.fraud_detection import fraud_detector
from services.mongodb_service import mongo_service

def process_transaction(transaction):
    is_fraud = fraud_detector.detect_fraud(transaction)
    if not is_fraud:
        mongo_service.save_transaction(transaction)

if __name__ == "__main__":
    print("Starting Kafka consumer...")
    kafka_service.consume_messages("transactions", process_transaction)
