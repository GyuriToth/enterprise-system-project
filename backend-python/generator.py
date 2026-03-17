import requests
import time
import random

# API endpoint
API_URL = "http://localhost:8000/transactions"

# Test data
users = ["Gyuri", "Alice", "Bob", "Charlie", "David", "Emma"]
currencies = ["HUF", "USD", "EUR", "GBP"]

print("Transaction generator started... (Ctrl+C to stop)")

try:
    while True:
        # Random data generation
        payload = {
            "user": random.choice(users),
            "amount": round(random.uniform(10.0, 5000.0), 2),
            "currency": random.choice(currencies)
        }

        # Sending to API
        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                print(f"Saved: {payload['user']} - {payload['amount']} {payload['currency']}")
            else:
                print(f"Error: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

        # Wait a bit before the next transaction
        time.sleep(1) 

except KeyboardInterrupt:
    print("\nGenerator stopped.")