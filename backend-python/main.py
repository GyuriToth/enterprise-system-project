from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import database
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter

FRAUD_COUNTER = Counter('fraud_attempts_total', 'Gyanús tranzakciók száma')

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Transaction Monitor API")
Instrumentator().instrument(app).expose(app)

class TransactionCreate(BaseModel):
    user: str
    amount: float
    currency: str

@app.post("/transactions")
def create_transaction(transaction: TransactionCreate, db: Session = Depends(database.get_db)):
    # --- CSALÁSFIGYELŐ LOGIKA (Fraud Detection) ---
    # Példa: Ha az összeg nagyobb, mint 4000, jelöljük gyanúsnak
    is_fraud = False
    if transaction.amount > 4000:
        FRAUD_COUNTER.inc() # Megnöveljük a csalás-számlálót
        is_fraud = True
        status_to_save = "flagged" # 'flagged' státusszal mentjük el
    else:
        status_to_save = "completed"

    db_transaction = models.Transaction(
        user=transaction.user,
        amount=transaction.amount,
        currency=transaction.currency,
        status=status_to_save
    )
    
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    
    return {
        "message": "Transaction processed", 
        "id": db_transaction.id, 
        "fraud_alert": is_fraud # Visszajelzünk az API hívónak is
    }

@app.get("/")
def read_root():
    return {"status": "online", "message": "Backend is connected to Postgres!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/transactions")
def create_transaction(transaction: TransactionCreate, db: Session = Depends(database.get_db)):
    db_transaction = models.Transaction(
        user=transaction.user,
        amount=transaction.amount,
        currency=transaction.currency,
        status="completed"
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return {"message": "Transaction saved!", "id": db_transaction.id}