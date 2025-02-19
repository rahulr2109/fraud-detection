from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB_NAME

class MongoDBService:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DB_NAME]
        self.transactions = self.db["transactions"]
        self.fraud_alerts = self.db["fraud_alerts"]

    def save_transaction(self, transaction):
        self.transactions.insert_one(transaction)

    def save_fraud_alert(self, alert):
        self.fraud_alerts.insert_one(alert)

    def get_transactions(self, days):
        from datetime import datetime, timedelta
        start_date = datetime.utcnow() - timedelta(days=days)
        return list(self.transactions.find({"timestamp": {"$gte": start_date}}, {"_id": 0}))

mongo_service = MongoDBService()

if __name__ == "__main__":
    print("mongo_service:", mongo_service)

