import requests

url = "https://api.ciscospark.com/v1/webhooks"

payload = "{\r\n  \"resource\" : \"messages\",\r\n  \"event\" : \"created\",\r\n  \"filter\" : \"roomId=Y2lzY29zcGFyazovL3VzL1JPT00vZDUyOWQyYjAtYTNkYy0xMWU3LWI5NmYtNWZiY2I3ZjUxYWEx\",\r\n  \"targetUrl\" : \"https://requestb.in/1dvgs9p1\",\r\n  \"name\" : \"Spark Learning Lab Webhook\"\r\n}"
headers = {
    'content-type': "application/json; charset=utf-8",
    'authorization': "Bearer Your_Access_Token",
    'cache-control': "no-cache",
    'postman-token': "9dbd51fe-57f6-a5cb-12be-4e5deb25bbc3"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)