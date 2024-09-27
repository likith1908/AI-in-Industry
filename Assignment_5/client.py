import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 1883
topic = "test/topic"
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.publish(topic, "Hello from client!")
def on_publish(client, userdata, mid):
    print("Message published.")

client = mqtt.Client()

client.on_connect = on_connect
client.on_publish = on_publish

client.connect(broker, port, 60)

client.loop_start()

client.publish(topic, "This is a test message.")

import time
time.sleep(2)

client.loop_stop()
client.disconnect()
