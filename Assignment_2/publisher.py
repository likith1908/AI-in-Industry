import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://15.207.98.49:5555")

while True:
    topic = "topic1"
    message = "Hello from publisher"
    socket.send_string(f"{topic} {message}")
    print(f"Published: {message}")
    time.sleep(1)
