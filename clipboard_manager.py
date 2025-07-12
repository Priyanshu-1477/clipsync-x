import time
import pyperclip
import threading
from datetime import datetime

class ClipboardManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ClipboardManager, cls).__new__(cls)
            cls._instance.history = []
            cls._instance.last_clipboard = None
            cls._instance.running = False
        return cls._instance

    def listen(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.monitor, daemon=True).start()

    def monitor(self):
        print(f"[Clipboard] Tracking: {len(self.history)} items")
        while self.running:
            try:
                current = pyperclip.paste()
                if current != self.last_clipboard and current.strip():
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    self.history.append((timestamp, current))
                    self.last_clipboard = current

                    if len(self.history) > 20:
                        self.history.pop(0)
            except Exception as e:
                print(f"[Clipboard Error] {e}")
            time.sleep(0.5)

    def get_history(self):
        return list(reversed(self.history))
