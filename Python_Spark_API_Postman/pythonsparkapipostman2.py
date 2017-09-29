# Import necessary modules
import requests
import json

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

# Define variables
url = "https://api.ciscospark.com/v1"
api_call = "/people"
access_token = "Bearer Your_Access_Token"

# Header information
headers = {
            "content-type" : "application/json; charset=utf-8",
            "authorization" : access_token
          }

# Parameter variable
user_email = input("What's the email you were looking for: ")
param = "?email=" + user_email

# Combine URL, API call and parameters variables
url += api_call + param

# Get the result
response = requests.get(url, headers=headers, verify=False).json()

# Print the respond body
# print(response.text)

# Print user's name and email address from respond body
for item in response["items"]:
    print("Name: " + item["displayName"])
    print("Email: " + item["emails"][0])
