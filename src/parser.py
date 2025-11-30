import re


def parse_log_line(line):
    if "ERROR" in line:
        return "ERROR"
    elif "WARNING" in line:
        return "WARNING"
    elif "INFO" in line:
        return "INFO"
    return None
