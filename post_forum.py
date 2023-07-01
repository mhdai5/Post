import requests
import os


with open("token.txt", "r") as f:
    token = f.read()

ACCESS_TOKEN = token
SCOPE_ID = 536351000000002008
TITLE = "test-aa%E3%81%95%E3%82%93"


with open("test.txt", "r") as file:
    CONTENT = file.read()


url = "https://connect.zoho.com/pulse/api/addBlog"


headers = {
    "Authorization": "Zoho-oauthtoken " + ACCESS_TOKEN,
    "Content-Type": "application/json"
}


params = {
    "scopeID": SCOPE_ID,
    "title": TITLE,
    "content": CONTENT,
    "disableComments": "true",
    "isPublished": "true"
}


response = requests.post(url, headers=headers, params=params)


print(response.json())
