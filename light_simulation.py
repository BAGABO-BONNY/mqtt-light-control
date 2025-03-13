import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe("/student_group/light_control")

def on_message(client, userdata, msg):
    status = msg.payload.decode()
    if status == "ON":
        print("💡 Light is TURNED ON")
    elif status == "OFF":
        print("⚫ Light is TURNED OFF")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)
client.loop_forever()
