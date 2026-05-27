from flask import Flask, jsonify
import psutil
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    return f"""
    <html>
    <head>
        <title>Cloud Monitoring Dashboard</title>
        <meta http-equiv="refresh" content="5">
    </head>

    <body style="font-family:Arial; text-align:center; margin-top:40px;">

        <h1>AWS Cloud Monitoring Dashboard</h1>

        <h2>EC2 Server Health</h2>

        <p><b>CPU Usage:</b> {cpu}%</p>

        <p><b>Memory Usage:</b> {memory}%</p>

        <p><b>Disk Usage:</b> {disk}%</p>

        <p><b>Updated:</b> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>

        <p style="color:green;"><b>Status: Healthy</b></p>

    </body>
    </html>
    """

@app.route("/health")
def health():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    return jsonify({
        "status": "healthy",
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)