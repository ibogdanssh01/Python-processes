# 🧠 Python-Processes

A cross-platform Python desktop application for **real-time process monitoring**, **weekly usage statistics**, and **productivity insights**—designed as a modern, intelligent alternative to the traditional Task Manager.

![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-blue)
![License](https://img.shields.io/github/license/ibogdanssh01/Python-Processes)
![Built with](https://img.shields.io/badge/built%20with-Python%20%7C%20PyQt6%20%7C%20psutil%20%7C%20orjson-informational)

---

## 📌 Features

- 🔍 **Process Monitoring:** See what applications and processes are running in real-time.
- 📊 **App Usage Stats:** Track how much time you've spent on each application weekly.
- 💾 **Efficient Storage:** Uses `orjson` for fast and lightweight JSON logging.
- 💡 **Smart Categorization:** Classifies processes into user apps, system processes, and more.
- 🧠 **Productivity Insights (Planned):** Future integration of an AI assistant to suggest time optimizations and reduce digital distractions.
- 📈 **Grafana/DB Integration:** Planned PostgreSQL backend for data analytics and visualization via Grafana.

---

## 🖥️ Demo

Coming soon – A GIF or video demo will be added once the GUI and dashboard are finalized.

---

## 🛠️ Technologies Used

| Tool        | Purpose                                      |
|-------------|----------------------------------------------|
| Python 3.10+ | Core programming language                    |
| psutil       | System process data and statistics           |
| orjson       | Fast JSON serialization/deserialization      |
| PyQt6        | GUI development framework                    |
| PostgreSQL   | (Planned) persistent data storage            |
| Grafana      | (Planned) visualization of usage stats       |

---

## 🗂️ Project Structure

```
Python-processes/
├── .github/                 # GitHub Actions workflow
│   └── workflows/
├── configuration_files/     # JSON-based rules and settings
│   ├── config.json
│   └── rules.json
├── output/                  # Logged data (e.g., process stats)
│   └── processes.json
├── src/
│   ├── config/              # Local config logic
│   ├── core/
│   │   └── python_processes/
│   │       ├── dataclasses.py
│   │       ├── enums.py
│   │       └── python_processes.py
│   ├── gui/
│   │   ├── assets/          # Icons, images
│   │   ├── output/          # GUI-generated data
│   │   ├── ui/              # UI layout and widgets
│   │   └── guiApp.py        # Main GUI application
│   ├── output/              # Other output files
│   ├── main.py              # Main entry point
│   └── tests/
│       └── __init__.py
├── LICENSE
├── pyproject.toml
├── README.md
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ibogdanssh01/Python-Processes.git
cd Python-Processes
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/MacOS
.venv\Scripts\activate       # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python src/main.py
```

---

## 💡 Example Use Case

> Want to know how much time you've spent in VSCode or Chrome this week?
> Open the app. Let it run silently in the background.
> Come back at the end of the week and analyze your usage in detail.

---

## 🧩 Roadmap

- [ ] PostgreSQL storage layer
- [ ] Grafana dashboard integration
- [ ] AI assistant to help you reduce app distractions
- [ ] Weekly and daily summary exports (PDF/CSV)
- [ ] Notifications for time limits

---

## 📚 Related Projects

- [FlashingEcuOTA](https://github.com/ibogdanssh01/FlashingEcuOTA) — OTA Flashing system for automotive ECUs.
- [FerrixOX (WIP)](https://github.com/ibogdanssh01/FerrixOX) — Rust-based hobby operating system.

---

## 👨‍💻 Authors

**Bogdan-Teodor Constantin (ibogdanssh) - Project creator and primary maintainer (Co-owner)**

Python Developer • Automation Enthusiast
- 📧 [bogdanteodor.constantin@gmail.com](mailto:bogdanteodor.constantin@gmail.com)
- 🔗 [LinkedIn](https://www.linkedin.com/in/bogdan-teodor-constantin/)
- 🔗 [Github](https://github.com/ibogdanssh01)

**Rotaru Stefan (rotarustef) - Collaborator and co-maintainer**
- 🔗[Github](https://github.com/rotarustef)
- 🔗[LinkedIn](https://www.linkedin.com/in/stefan-rotaru-3b21691bb/)


---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
