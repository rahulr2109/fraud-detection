import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from services.mongodb_service import mongo_service
from services.redis_service import redis_service
from services.kafka_service import kafka_service
from api.websocket_routes import manager

class FraudDetection:
    def __init__(self):
        self.model = self.train_model()

    def train_model(self):
        data = list(mongo_service.transactions.find({}, {"_id": 0}))
        if len(data) < 100:
            return None  # Not enough data to train

        df = pd.DataFrame(data)
        model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
        model.fit(df[['amount', 'balance_before', 'balance_after']])
        return model

    async def detect_fraud(self, transaction):
        if not self.model:
            return False

        features = pd.DataFrame(
            [[transaction["amount"], transaction["balance_before"], transaction["balance_after"]]],
            columns=["amount", "balance_before", "balance_after"]
        )
        prediction = self.model.predict(features)

        if prediction[0] == -1:
            mongo_service.save_fraud_alert(transaction)
            redis_service.save_fraud_alert(transaction["transaction_id"], transaction)
            kafka_service.send_message("fraud-alerts", transaction)
            await manager.broadcast(transaction)

            return True
        return False

# Create an instance that should be importable as "fraud_detector"
fraud_detector = FraudDetection()
