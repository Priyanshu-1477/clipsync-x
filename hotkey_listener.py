import threading
import keyboard

class HotkeyListener:
    def __init__(self, on_activate, combo="ctrl+alt+v"):
        self.on_activate = on_activate
        self.combo = combo

    def start(self):
        def listen():
            keyboard.add_hotkey(self.combo, self.on_activate)
            keyboard.wait()  # keeps this thread alive

        thread = threading.Thread(target=listen, daemon=True)
        thread.start()
