# Import necessary modules
import requestsimport json

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

# Define variables
url = "https://api.ciscospark.com/v1"
api_call = "/rooms"
access_token = "Your_Access_Token"

# Header information
headers = {
            "content-type" : "application/json; charset=utf-8",
            "authorization" : "Bearer " + access_token
          }

# Parameter variable
params = {"type" : "group", "max" : "2"}

# Combine URL, API call and parameters variables
url += api_call

# Get the result
response = requests.get(url=url, headers=headers, params=params)

# Print respons status and body
print(response.status_code)
print(response.text)
