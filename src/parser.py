# src/parser.py

def parse_log(log_file):
    errors = 0
    warnings = 0
    info = 0

    try:
        with open(log_file) as f:
            for line in f:
                line = line.strip()
                if "ERROR" in line:
                    errors += 1
                elif "WARNING" in line:
                    warnings += 1
                elif "INFO" in line:
                    info += 1
    except FileNotFoundError:
        print(f"Log file {log_file} not found.")

    return errors, warnings, info
