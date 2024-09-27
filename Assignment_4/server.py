import zmq
import time

context = zmq.Context()
server = context.socket(zmq.PAIR)
server.bind("tcp://0.0.0.0:5555")
print("Server is waiting for messages...")

while True:
    message = server.recv_string()
    print(f"Server received: {message}")
    
    response = f"Response to: {message}"
    server.send_string(response) 
    print(f"Server sent: {response}")
    time.sleep(1)
