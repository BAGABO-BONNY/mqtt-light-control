MQTT Light Control Application
A web-based application that demonstrates IoT light control using MQTT protocol. This project includes an interactive web interface with a visual light bulb simulation and a Python script that simulates an ESP8266 device responding to MQTT commands.

MQTT Light Control Demo

Features
Interactive web interface with animated light bulb
Real-time MQTT communication
ON/OFF control with visual feedback
Light bulb flicker animation when turned on
Simulated IoT device using Python
Project Components
index.html: Web interface with visual light bulb and control buttons
light_simulation.py: Python script simulating an ESP8266 device
README.md: Project documentation
Technical Details
Uses MQTT.js for browser-based MQTT communication over WebSockets
Uses Paho MQTT for Python-based device simulation
Communicates with MQTT broker at 157.173.101.159
Publishes commands to /student_group/light_control topic
Subscribes to status updates on /student_group/light_status topic
Setup Instructions
Prerequisites
Web browser with JavaScript enabled
Python 3.x with paho-mqtt library
Access to the MQTT broker at 157.173.101.159
Running the Web Interface
Open index.html in a web browser
The interface will automatically connect to the MQTT broker via WebSockets (port 9001)
Use the "Turn ON" and "Turn OFF" buttons to control the light
Running the Simulated IoT Device
Install the required Python package:

pip install paho-mqtt
Run the simulation script:

python light_simulation.py
The script will connect to the MQTT broker (port 1883) and respond to commands

MQTT Topics
/student_group/light_control: Used to send ON/OFF commands to the device
/student_group/light_status: Used to receive status updates from the device
How It Works
The web interface publishes "ON" or "OFF" commands to the /student_group/light_control topic
The simulated IoT device (Python script) receives these commands and processes them
The device publishes the current state back to the /student_group/light_status topic
The web interface updates the visual light bulb based on the status messages
Troubleshooting
If the web interface doesn't connect, check that the MQTT broker is running and accessible
Ensure port 9001 (WebSockets) is open for the web interface
Ensure port 1883 (MQTT) is open for the Python script
Check browser console for any connection errors
License
MIT License

Acknowledgments
MQTT.js library for browser-based MQTT communication
Paho MQTT for Python client implementation