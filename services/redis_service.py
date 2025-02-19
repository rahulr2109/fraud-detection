import redis
import json
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

class RedisService:
    def __init__(self):
        self.client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD,
            decode_responses=True
        )

    def save_fraud_alert(self, transaction_id, alert):
        # Save alert with an expiry of 86400 seconds (24 hours)
        self.client.set(f"fraud_alert:{transaction_id}", json.dumps(alert), ex=86400)

    def get_fraud_alerts(self):
        keys = self.client.keys("fraud_alert:*")
        return [json.loads(self.client.get(k)) for k in keys]

# Create an instance that can be imported elsewhere
redis_service = RedisService()
