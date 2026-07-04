"""
metrics-collector.py
Polls system stats + website health every 10s and sends them to Graphite (Carbon)
so Grafana can chart: CPU, Memory, Network Usage, HTTP Availability, Uptime.

Requirements: pip install psutil requests
Run:          python3 metrics-collector.py
"""
import socket
import time
import psutil
import requests

GRAPHITE_HOST = "localhost"
GRAPHITE_PORT = 2003
WEBSITE_URL = "http://localhost:30080/health"
INTERVAL_SECONDS = 10

START_TIME = time.time()


def send_metric(sock, path, value, timestamp):
    message = f"{path} {value} {int(timestamp)}\n"
    sock.sendall(message.encode("utf-8"))


def check_website_up():
    try:
        r = requests.get(WEBSITE_URL, timeout=3)
        return 1 if r.status_code == 200 else 0
    except requests.RequestException:
        return 0


def main():
    while True:
        timestamp = time.time()
        cpu_percent = psutil.cpu_percent(interval=1)
        mem_percent = psutil.virtual_memory().percent
        net = psutil.net_io_counters()
        http_up = check_website_up()
        uptime_seconds = timestamp - START_TIME

        try:
            with socket.create_connection((GRAPHITE_HOST, GRAPHITE_PORT), timeout=5) as sock:
                send_metric(sock, "abc_website.system.cpu_percent", cpu_percent, timestamp)
                send_metric(sock, "abc_website.system.memory_percent", mem_percent, timestamp)
                send_metric(sock, "abc_website.network.bytes_sent", net.bytes_sent, timestamp)
                send_metric(sock, "abc_website.network.bytes_recv", net.bytes_recv, timestamp)
                send_metric(sock, "abc_website.http.availability", http_up, timestamp)
                send_metric(sock, "abc_website.uptime_seconds", uptime_seconds, timestamp)
            print(f"[OK] cpu={cpu_percent}% mem={mem_percent}% http_up={http_up}")
        except (ConnectionRefusedError, OSError) as e:
            print(f"[WARN] Could not reach Graphite: {e}")

        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
