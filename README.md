# MQTT Light Control

This project is a simple **MQTT-based Light Control System** using **Python (Flask + Paho MQTT)** and **HTML**. It allows users to turn a light ON or OFF via a web interface, with Python handling MQTT communication.

---

## 📌 Features
✅ Web-based control panel (HTML + Flask)
✅ MQTT-based light control
✅ No JavaScript required
✅ Uses HiveMQ public broker
✅ Flask handles button clicks and publishes MQTT messages

---

## 🛠 Requirements
Ensure you have the following installed:

- **Python 3**
- Flask
- Paho-MQTT

To install dependencies, run:
```bash
pip install flask paho-mqtt
```

---

## 🚀 Running the Project
### 1️⃣ Start the Flask Server
Run the following command:
```bash
python mqtt_light_control.py
```
The server will start at `http://localhost:5000`.

### 2️⃣ Open the Web Interface
- Open a browser and go to `http://localhost:5000`.
- Click **Turn ON** or **Turn OFF** to send an MQTT message.

---

## 📜 Project Structure
```
📂 mqtt-light-control
├── 📄 mqtt_light_control.py  # Python Flask server & MQTT logic
├── 📄 templates/
│   ├── 📄 index.html         # Web interface (UI)
├── 📄 README.md             # Documentation
```

---

## ⚡ How It Works
1. **Flask serves the web page** (`index.html`).
2. **User clicks a button** → Sends a request to Flask.
3. **Flask publishes an MQTT message** (`ON` or `OFF`) to `/student_group/light_control`.
4. **MQTT client publishes the message** to the HiveMQ broker.
5. **Any MQTT subscriber** (like a light controller) receives the message and toggles the light.

---
MQTT Light Control
This project implements a simple MQTT-based light control system using Python and HTML. The Python script listens for messages from an MQTT broker and updates the light status accordingly.

📌 Features
Python-based MQTT client that subscribes to light control messages.
HTML front-end to provide a simple UI (but no JavaScript logic).
Uses MQTT protocol for real-time communication.
Supports turning the light ON or OFF using MQTT messages.
📂 Project Structure
bash
Copy
Edit
/mqtt-light-control
│── index.html        # Front-end UI (No JavaScript)
│── light_control.py  # Python MQTT subscriber & handler
└── README.md         # Documentation
⚙️ Requirements
Ensure you have Python 3.x installed along with the required package:

sh
Copy
Edit
pip install paho-mqtt
🚀 How to Run
Start the Python MQTT client:

sh
Copy
Edit
python light_control.py
This will connect to the MQTT broker and listen for messages.

Send MQTT messages to control the light:

Use an external MQTT client (e.g., MQTT Explorer, mosquitto_pub) to publish messages to the topic:

sh
Copy
Edit
mosquitto_pub -h broker.hivemq.com -t "/student_group/light_control" -m "ON"
mosquitto_pub -h broker.hivemq.com -t "/student_group/light_control" -m "OFF"
View the HTML page (index.html) in a browser. (Note: Since JavaScript is removed, the UI will not update automatically.)

🔧 Future Improvements
Add a Python web server (e.g., Flask) to serve dynamic updates.
Implement an embedded display or physical LED control.
Use a local MQTT broker for better reliability.
## 📝 Notes
- You can change the MQTT broker in `mqtt_light_control.py`.
- This project uses **HiveMQ public broker** (free).
- Modify the MQTT topic `/student_group/light_control` as needed.

---

## 🤖 Future Improvements
- Add real-time MQTT status updates on the web UI.
- Secure the web interface with authentication.
- Use a local MQTT broker for private networks.

---

## 📧 Need Help?
If you have any questions, feel free to ask! 🚀