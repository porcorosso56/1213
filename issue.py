import json
import requests

print("enter repo name")
name = input()
api = "https://api.github.com/search/issues?q=repo:"
issueType = "+type:issue+state:"
print("enter issue type(open or closed)")
state = input()
url = api+name+issueType+state
response = requests.get(url)
data = response.json()

print(data["total_count"])
