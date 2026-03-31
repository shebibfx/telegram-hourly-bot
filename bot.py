import requests
import time
from datetime import datetime, timedelta

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_message():
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": CHAT_ID,
            "text": "Check market candle"
        }
        requests.post(url, data=data)
        print("Sent at:", datetime.now())
    except Exception as e:
        print("Error:", e)

def wait_until_next_hour():
    now = datetime.now()
    next_hour = (now.replace(minute=0, second=0, microsecond=0) 
                 + timedelta(hours=1))
    sleep_seconds = (next_hour - now).total_seconds()
    time.sleep(sleep_seconds)

# Main loop
while True:
    wait_until_next_hour()  # wait until :00
    send_message()