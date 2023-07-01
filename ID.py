import requests
import json
with open("token.txt", "r") as f:
    token = f.read()
    print(token)
# Zoho OAuth token
oauth_token = token

# API URL
url = "https://connect.zoho.com/pulse/api/allScopes"

# Headers
headers = {
    "Authorization": f"Zoho-oauthtoken {oauth_token}",
}

# Send the request
response = requests.get(url, headers=headers)

# Make sure the request was successful
response.raise_for_status()

# Parse the JSON response
data = response.json()

# Extract the network IDs
network_ids = [network["id"] for network in data["allScopes"]["scopes"]]

print(network_ids)
