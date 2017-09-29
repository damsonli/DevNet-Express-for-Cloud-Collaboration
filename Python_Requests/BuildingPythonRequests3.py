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

# Combine URL, API call and parameters variables
url += api_call

# Post markdown messages
markdown = ["**Warning!!!**",
            "*Warning!!!*",
            "[Danger, Will Robinson!!!](https://en.wikipedia.org/wiki/Lost_in_Space#Catchphrases)"]

for message in markdown:
    payload = {"toPersonEmail": "adventure@sparkbot.io", "markdown": message}
    response = requests.post(url=url, json=payload, headers=headers)

    print(response.status_code)
    print(response.text)