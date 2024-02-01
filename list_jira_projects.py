# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://venu-devops.atlassian.net/rest/api/3/project"
# Passing api_token and mail_id as environment variables using export command in command-line
api_token = os.getenv("api_token")
mail_id = os.getenv("mail_id")
auth = HTTPBasicAuth(mail_id, api_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
result = json.loads(response.text)
num_of_items = len(result)
print("Projects in Jira are: ")
for item in range(num_of_items):
  project_name = result[item]["name"]
  print(project_name)