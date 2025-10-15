# Just As Rather Very Intelligent System (J.A.R.V.I.S.)

**Version:** 1.0
**Author:** Jenis Das

---

## **Overview**

J.A.R.V.I.S. (Just As Rather Very Intelligent System) is a modular AI assistant designed to automate tasks, interact with IoT devices, and enhance productivity. It combines **Windows automation**, **IoT control**, **audio interaction**, and **web capabilities** in one intelligent system.

This system is built to be **extensible**, **maintainable**, and **grounded in modular architecture**.

---

## **Features**

* **Windows Automation (Apps folder)**: Automates common tasks on Windows OS.
* **IoT Automation (Auto folder)**: Controls IoT devices, sensors, and home automation.
* **Audio Interaction (Sound folder)**: Handles voice input/output for natural communication.
* **Web Modules (Web folder)**: Scrapes data, interacts with web services, or handles browser automation.
* **History Tracking (History folder)**: Maintains logs of AI-user interactions.
* **System Monitoring (System.py)**: Checks system status and sends warnings.
* **Keyword-Based Commands (keyWords.json)**: Parses user instructions efficiently.

---

## **Folder Structure**

```
JARVIS/
│
├─ APIs/          # External API integrations
├─ Apps/          # Windows automation scripts
├─ Auto/          # IoT automation scripts
├─ Docs/          # Documentation
├─ env/           # Virtual environment
├─ History/       # AI-user interaction logs
├─ Sound/         # Audio input/output
├─ Web/           # Web-related modules
│
├─ Controller.py  # Main orchestrator of modules
├─ Createhistory.py  # Logs interactions
├─ JARVIS.py      # Core AI logic
├─ Overall.py     # High-level integration
├─ System.py      # System checks and warnings
│
├─ keyWords.json  # Keywords for command parsing
└─ SystemChecks.json  # Status/config of system checks
```

---

## **Getting Started**

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/JARVIS.git
cd JARVIS
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Activate environment**

```bash
# Windows
.\env\Scripts\activate

# Linux / Mac
source env/bin/activate
```

4. **Run J.A.R.V.I.S.**

```bash
python Controller.py
```

---

## **Usage**

* Interact with J.A.R.V.I.S. via terminal or voice commands.
* Control Windows apps or IoT devices seamlessly.
* Commands are parsed from `keyWords.json` — you can add your own.

---

## **Future Improvements**

* Parameter-efficient AI fine-tuning for smarter responses.
* Integration of learning modules for adaptive behavior.
* GUI interface for easier access to Windows automation and IoT modules.
* Advanced logging and monitoring dashboard.

---

## **Contributing**

* Contributions are welcome!
* Please follow **modular coding principles** to keep the architecture clean.

---

## **License**

This project is **open-source**. You can use, modify, and distribute it under the MIT License.
