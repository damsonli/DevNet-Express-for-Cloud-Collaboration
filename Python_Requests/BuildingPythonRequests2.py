# Import necessary modules
import requests

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

# Define variables
url = "https://api.ciscospark.com/v1"
api_call = "/messages"
access_token = "Your_Access_Token"

# Header information
headers = {
            "content-type" : "application/json; charset=utf-8",
            "authorization" : "Bearer " + access_token
          }

# Payload variable
payload = {"toPersonEmail" : "adventure@sparkbot.io", "text" : "Hello"}

# Combine URL, API call and parameters variables
url += api_call

# Post the message
response = requests.post(url=url, headers=headers, json=payload)

# Print respons status and body
print(response.status_code)
print(response.text)
