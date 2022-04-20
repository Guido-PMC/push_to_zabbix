import requests
import time
time.sleep(10)
url = "http://192.168.10.3:5000/wallet/0xe68702d72e47fd1ad5cbe5a0bc6911500b91eefd"

payload={}
headers = {
  'api_key': '48d69e24-6723-484a-988b-be1da234848f'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
