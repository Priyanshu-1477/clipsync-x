import os
os.environ["QT_QPA_PLATFORM"] = "xcb"

import sys
import pyperclip
import threading
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QLabel, QScrollArea
)
from PyQt5.QtCore import QTimer
from clipboard_manager import ClipboardManager
from pynput import keyboard

clipboard = ClipboardManager()
clipboard.listen()

app = QApplication(sys.argv)
window = None
paste_window = None
pending_show_gui = False
pending_show_paste = False

class ClipSyncX(QWidget):
    def __init__(self, clipboard):
        super().__init__()
        self.clipboard = clipboard
        self.setWindowTitle("ClipSync X - Clipboard God")
        self.setGeometry(500, 200, 400, 500)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.update_ui()

    def update_ui(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        self.layout.addWidget(QLabel("📋 Clipboard History:"))

        scroll = QScrollArea()
        content = QWidget()
        vbox = QVBoxLayout()

        for timestamp, item in self.clipboard.get_history():
            btn = QPushButton(f"[{timestamp}] {item[:50]}")
            btn.clicked.connect(lambda _, text=item: pyperclip.copy(text))
            vbox.addWidget(btn)

        content.setLayout(vbox)
        scroll.setWidget(content)
        scroll.setWidgetResizable(True)
        self.layout.addWidget(scroll)

class PasteSelector(QWidget):
    def __init__(self, clipboard):
        super().__init__()
        self.clipboard = clipboard
        self.setWindowTitle("🧠 Paste from History")
        self.setGeometry(600, 300, 400, 400)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.build_ui()

    def build_ui(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for timestamp, item in self.clipboard.get_history():
            btn = QPushButton(f"[{timestamp}] {item[:50]}")
            btn.clicked.connect(lambda _, text=item: self.paste_text(text))
            self.layout.addWidget(btn)

    def paste_text(self, text):
        pyperclip.copy(text)
        self.hide()
        QTimer.singleShot(200, lambda: print("✅ Text copied. You can now paste it anywhere."))

def safe_show_gui():
    global window
    if window:
        window.close()
    window = ClipSyncX(clipboard)
    window.show()

def safe_show_paste_selector():
    global paste_window
    if paste_window:
        paste_window.close()
    paste_window = PasteSelector(clipboard)
    paste_window.show()

def trigger_gui_popup():
    global pending_show_gui
    pending_show_gui = True

def trigger_paste_popup():
    global pending_show_paste
    pending_show_paste = True

def check_pending_windows():
    global pending_show_gui, pending_show_paste
    if pending_show_gui:
        safe_show_gui()
        pending_show_gui = False
    if pending_show_paste:
        safe_show_paste_selector()
        pending_show_paste = False
    QTimer.singleShot(100, check_pending_windows)

def listen_to_hotkeys():
    COMBO_VIEW = {keyboard.Key.ctrl_l, keyboard.Key.alt_l, keyboard.KeyCode(char='v')}
    COMBO_PASTE = {keyboard.Key.ctrl_l, keyboard.Key.alt_l, keyboard.KeyCode(char='b')}
    current_keys = set()

    def on_press(key):
        current_keys.add(key)
        if all(k in current_keys for k in COMBO_VIEW):
            trigger_gui_popup()
        elif all(k in current_keys for k in COMBO_PASTE):
            trigger_paste_popup()

    def on_release(key):
        current_keys.discard(key)

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

# Start hotkey listener thread
threading.Thread(target=listen_to_hotkeys, daemon=True).start()
QTimer.singleShot(100, check_pending_windows)

print("✅ ClipSync X running in background.")
sys.exit(app.exec_())
