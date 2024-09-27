import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUSH)

socket.connect("tcp://15.207.98.49:5555")
for task_num in range(10):
    message = f"Task {task_num}"
    print(f"Sending: {message}")
    socket.send_string(message)
    time.sleep(1)

print("All tasks have been sent.")
