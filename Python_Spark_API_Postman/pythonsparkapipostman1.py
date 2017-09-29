import requests

url = "https://api.ciscospark.com/v1/rooms"

headers = {
    'content-type': "application/json; charset=utf-8",
    'authorization': "Bearer Your_Access_Token",
    'cache-control': "no-cache",
    'postman-token': "fda95265-983b-d330-c3e0-e10f0c49ff68"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)