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