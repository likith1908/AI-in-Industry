import requests

url = "http://15.207.98.49:5000/api/messages"
data = {
    "message": "Likith"
}

response = requests.post(url, json=data)

print(response.text)
