import requests
from flask import Flask
import os

app = Flask(__name__)

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_message():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": "Check market candle"
    }
    requests.post(url, data=data)

@app.route("/")
def home():
    return "Bot is alive"

@app.route("/send")
def trigger():
    send_message()
    return "k"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
