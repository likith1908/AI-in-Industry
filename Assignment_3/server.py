import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://0.0.0.0:5555")
print("Waiting for tasks...")

while True:
    message = socket.recv_string()
    print(f"Received: {message}")
