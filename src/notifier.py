# src/notifier.py
import requests


def send_alert(webhook_url, message):
    payload = {"text": message}
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print("Alert sent successfully")
        else:
            print("Failed to send alert:", response.status_code)
    except Exception as e:
        print("Error sending alert:", e)
