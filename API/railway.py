# Indian Railways API Example
import requests

url = "http://api.erail.in/"
headers = {
    "Content-Type": "application/json"
}

response = requests.get(url)
data = response.json()
print(data)