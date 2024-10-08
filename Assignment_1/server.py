from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/messages', methods=['POST'])
def receive_message():
    data = request.json
    message = data.get('message', '')
    print(f"Received message: {message}")
    return jsonify({"status": "Message received!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
