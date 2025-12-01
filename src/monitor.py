# src/monitor.py
import csv
import json
import time
from datetime import date

import schedule

from .notifier import send_alert
from .parser import parse_log

# Load configuration
with open("config.json") as f:
    config = json.load(f)

log_file = config["log_file"]
webhook_url = config["webhook_url"]
metrics_file = config["metrics_file"]
error_threshold = config["error_threshold"]

def save_metrics(errors, warnings, info):
    today = date.today().isoformat()
    try:
        with open(metrics_file, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([today, errors, warnings, info])
    except Exception as e:
        print("Error writing metrics:", e)

def monitor_logs():
    errors, warnings, info = parse_log(log_file)
    print(f"Errors: {errors}, Warnings: {warnings}, Info: {info}")
    
    if errors >= error_threshold:
        send_alert(webhook_url, f"{errors} errors detected!")
    
    save_metrics(errors, warnings, info)

# Run every 1 minute
schedule.every(1).minutes.do(monitor_logs)

print("Log monitor started...")
while True:
    schedule.run_pending()
    time.sleep(1)
