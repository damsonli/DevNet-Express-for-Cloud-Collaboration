import requests,datetime,json

ut = "Number of days to New Year: " + str((datetime.date(2018,1,1)-datetime.date.today()).days)
body = {"roomId" : "Y2lzY29zcGFyazovL3VzL1JPT00vZDUyOWQyYjAtYTNkYy0xMWU3LWI5NmYtNWZiY2I3ZjUxYWEx", "text" : ut}
headers = {
    "Authorization": "Bearer Your_Access_Token",
    "Content-Type": "application/json"
    }
requests.request("POST", url="https://api.ciscospark.com/v1/messages",
    data=json.dumps(body), headers=headers)
