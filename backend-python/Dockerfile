# image
FROM python:3.11-slim

# WORKDIR
WORKDIR /app    

# dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# code copy
COPY . .

# start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]