import requests

url = "https://apis.datura.ai/twitter"

payload = {"query": "crypto"}
headers = {
    "Authorization": "REMOVED",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)