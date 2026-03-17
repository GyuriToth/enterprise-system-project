from fastapi import FastAPI

app = FastAPI(title="Transaction Monitor API")

@app.get("/")
def read_root():
    return {"status": "online", "message": "Transaction Monitor Backend is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}