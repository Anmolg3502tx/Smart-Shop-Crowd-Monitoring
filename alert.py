import requests
import time
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, SHOP_NAME, COOLDOWN_MINUTES

last_alert_time = 0

def send_alert(people_count):
    global last_alert_time
    current_time = time.time()
    
    # Check cooldown
    if current_time - last_alert_time < COOLDOWN_MINUTES * 60:
        return
    
    message = (
        f"Alert from {SHOP_NAME}\n"
        f"High crowd detected!\n"
        f"People count: {people_count}\n"
        f"Please check the shop immediately."
    )
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    
    try:
        requests.post(url, json=payload)
        last_alert_time = current_time
        print(f"Alert sent. People count: {people_count}")
    except Exception as e:
        print(f"Alert failed: {e}")
