import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 1883
topic = "test/topic"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port, 60)
client.loop_start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
