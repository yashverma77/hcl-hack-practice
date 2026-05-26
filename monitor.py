import psutil
import time
from datetime import datetime

def monitor_system():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        log = (
            f"{datetime.now()} | "
            f"CPU: {cpu}% | "
            f"Memory: {memory}% | "
            f"Disk: {disk}%"
        )

        print(log)

        # save logs in file
        with open("system.log", "a") as file:
            file.write(log + "\n")

        # wait 5 seconds
        time.sleep(5)

if __name__ == "__main__":
    monitor_system()