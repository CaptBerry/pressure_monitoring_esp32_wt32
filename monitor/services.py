import threading
import time
import requests

from .models import Microcontroller

# Глобальный кэш с данными МК
controller_data_cache = {}

def fetch_data():
    while True:
        controllers = Microcontroller.objects.all()
        for controller in controllers:
            url = f"http://{controller.ip}/api"
            try:
                response = requests.get(url, timeout=1.5)
                data = response.json()

                # Статус
                t = data.get("temperature", 0)
                p = data.get("pressure", 0)
                status = "ok"
                if not (controller.min_temp <= t <= controller.max_temp):
                    status = "warn"
                if not (controller.min_pressure <= p <= controller.max_pressure):
                    status = "warn"

                controller_data_cache[controller.id_device] = {
                    "name": controller.name,
                    "t": t,
                    "p": p,
                    "status": status,
                    "ip": controller.ip,
                }
            except Exception:
                # Ошибка соединения
                controller_data_cache[controller.id_device] = {
                    "name": controller.name,
                    "status": "error",
                    "ip": controller.ip,
                }

        time.sleep(3)

def start_background_fetch():
    thread = threading.Thread(target=fetch_data, daemon=True)
    thread.start()
