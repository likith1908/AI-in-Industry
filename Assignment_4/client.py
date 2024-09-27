import zmq
import time

context = zmq.Context()
client = context.socket(zmq.PAIR)
client.connect("tcp://15.207.98.49:5555")

print("Client is sending messages...")

for i in range(5):
    message = f"Message {i}"
    client.send_string(message)
    print(f"Client sent: {message}")
    
    response = client.recv_string()  
    print(f"Client received: {response}")
    time.sleep(2)
