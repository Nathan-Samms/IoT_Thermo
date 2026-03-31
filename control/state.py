# control/state.py
import json
import os
import threading

from settings import STATE_FILE

_DEFAULT = {
    "last_angle": 90,
    "fan_on": False
}

class StateManager:
    def __init__(self, path=None):
        self.path = path or STATE_FILE
        self.lock = threading.Lock()
        self.state = _DEFAULT.copy()
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        self._load()

    def _load(self):
        try:
            if os.path.exists(self.path):
                with open(self.path, "r") as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        self.state.update(data)
        except Exception:
            self._save()

    def _save(self):
        with open(self.path, "w") as f:
            json.dump(self.state, f, indent=2)

    def get_angle(self):
        with self.lock:
            return float(self.state.get("last_angle", 90))

    def set_angle(self, angle):
        with self.lock:
            self.state["last_angle"] = float(angle)
            self._save()

    def get_fan(self):
        with self.lock:
            return bool(self.state.get("fan_on", False))

    def set_fan(self, on):
        with self.lock:
            self.state["fan_on"] = bool(on)
            self._save()

state = StateManager()
