count_errors = {}
error_message = {}
logs = [
    {"level": "INFO", "msg": "Started"},
    {"level": "ERROR", "msg": "DB connection failed"},
    {"level": "ERROR", "msg": "DB connection failed"},
    {"level": "WARN", "msg": "Retrying"},
    {"level": "INFO", "msg": "User logged in"},
    {"level": "ERROR", "msg": "File not found"},
    {"level": "WARN", "msg": "Low memory"},
    {"level": "INFO", "msg": "Process completed"},
    {"level": "ERROR", "msg": "Timeout occurred"},
    {"level": "WARN", "msg": "Deprecated API used"},
    {"level": "INFO", "msg": "Configuration loaded"},
    {"level": "ERROR", "msg": "Permission denied"},
    {"level": "WARN", "msg": "Disk space low"},
    {"level": "INFO", "msg": "Server started"}
]
for log in logs:
    level = log["level"]
    msg = log["msg"]
    if msg not in error_message and level == "ERROR":
        error_message[msg] = 1
        if level not in count_errors:
            count_errors[level] = 1
        elif level in count_errors:
            count_errors[level] += 1
    elif msg in error_message and level == "ERROR":
        error_message[msg] += 1
        if level not in count_errors:
            count_errors[level] = 1
        elif level in count_errors:
            count_errors[level] += 1
print(error_message)
print(count_errors.get("ERROR"))