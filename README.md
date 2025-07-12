# 🔗 ClipSync X – The Clipboard God

A modern, sleek, and powerful clipboard manager that runs silently in the background, tracks your copy history, and lets you paste anything you copied — **whenever you want**, with **hotkeys**. Designed like a pro system utility tool, it brings productivity and flair together.

> 📌 Press `Ctrl + Alt + V` to view clipboard history  
> 📌 Press `Ctrl + Alt + B` to directly paste from history  
> 🧠 Keeps your **last 20 clipboard items**  
> ⚙️ Runs as a **systemd user service** (auto-starts with system)

---

## 🚀 Features

- ✅ **Background clipboard tracking** (text-based)
- ✅ **System-wide hotkeys** to trigger GUI (no matter what app you're in)
- ✅ **View and copy any previous item** from history
- ✅ **Paste directly** using GUI pop-up
- ✅ **Clean PyQt5 GUI** – simple, fast, and useful
- ✅ **History capped to last 20** to keep things snappy
- ✅ **No sudo needed** – safe to run user-level
- ✅ **Systemd-ready** – auto-start on login, runs forever

---

## 🧪 Demo

<img src="https://user-images.githubusercontent.com/000000/clipboard-demo.gif" width="600" />

---

## 🛠 Tech Stack

- [Python 3](https://www.python.org/)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [pyperclip](https://pypi.org/project/pyperclip/)
- [pynput](https://pypi.org/project/pynput/)

---

## 📦 Installation

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/clipsync-x.git
cd clipsync-x
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run manually (for testing):**

```bash
python3 main.py
```

4. **Set up as systemd background utility (recommended):**

Create launcher script:

```bash
nano ~/.local/bin/clipsyncx-launcher.sh
```

Paste:

```bash
#!/bin/bash
export QT_QPA_PLATFORM=xcb
python3 /home/your_user/clipsync-x/main.py
```

Make executable:

```bash
chmod +x ~/.local/bin/clipsyncx-launcher.sh
```

Create systemd service:

```bash
nano ~/.config/systemd/user/clipsyncx.service
```

Paste:

```ini
[Unit]
Description=ClipSync X - Clipboard Tracker
After=graphical.target

[Service]
ExecStart=/home/your_user/.local/bin/clipsyncx-launcher.sh
Restart=always
Environment=DISPLAY=:0
Environment=XAUTHORITY=%h/.Xauthority

[Install]
WantedBy=default.target
```

Enable + start:

```bash
systemctl --user daemon-reload
systemctl --user enable clipsyncx.service
systemctl --user start clipsyncx.service
```

---

## 🎯 Usage

| Key Combo        | Action                      |
|------------------|-----------------------------|
| `Ctrl + Alt + V` | Show full clipboard history |
| `Ctrl + Alt + B` | Quick paste from history    |

✅ Click any item to copy it back to clipboard.

---

## 🔮 Future Scope

| Feature | Description |
|--------|-------------|
| 🌙 Dark Mode UI | Toggle dark/light theme from GUI |
| 📌 Pin Items | Prevent certain clipboard items from being removed |
| 🖼 Image Clipboard | Support and preview copied images |
| 🔄 Multi-Device Sync | Use FastAPI backend to sync across devices |
| ⏳ Clipboard Search | Quickly search clipboard history |
| 🔐 Secure Mode | Optionally encrypt clipboard history |
| 📊 Stats | Show copy frequency, patterns, etc. |
| 🧠 AI Assistant | Suggest paste completions based on context |

---

## 🤝 Contributing

Pull requests welcome! Feel free to suggest ideas, open issues, or build features.

---

## 📄 License

MIT License

---

## 👑 Author

Made with ❤️ by [Priyanshu Raj](https://github.com/Priyanshu-1477)  
Project idea + build by **you**, refined with ✨

---
