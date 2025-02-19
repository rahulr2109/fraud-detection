from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.mongodb_service import mongo_service
from services.redis_service import redis_service

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_fraud_alerts():
    return {"message": "Welcome to the Fraud Detection API!"}

@app.get("/transactions/{days}")
def get_transactions(days: int):
    return {"transactions": mongo_service.get_transactions(days)}

@app.get("/fraud-alerts/realtime")
def get_fraud_alerts():
    return {"fraud_alerts": redis_service.get_fraud_alerts()}
