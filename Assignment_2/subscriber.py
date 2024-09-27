import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://15.207.98.49:1883") 

socket.setsockopt_string(zmq.SUBSCRIBE, "topic1")

while True:
    message = socket.recv_string()
    print(f"Received: {message}")
