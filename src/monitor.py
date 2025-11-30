import json
import time
from parser import parse_log_line

from notifier import send_slack_alert


def tail_log(logfile, webhook):
    with open(logfile, "r") as f:
        f.seek(0, 2)  # Move to end of file
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue

            log_type = parse_log_line(line)

            if log_type == "ERROR":
                send_slack_alert(webhook, f"🚨 New ERROR found: {line.strip()}")
                print("Error alert sent!")

if __name__ == "__main__":
    config = json.load(open("config.json"))
    tail_log(config["log_file"], config["slack_webhook"])
