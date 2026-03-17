from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import database
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Transaction Monitor API")

class TransactionCreate(BaseModel):
    user: str
    amount: float
    currency: str

Instrumentator().instrument(app).expose(app)

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