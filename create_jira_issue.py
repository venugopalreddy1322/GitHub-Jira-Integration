# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://venu-devops.atlassian.net/rest/api/3/issue"
# Passing api_token and mail_id as environment variables using export command in command-line
api_token = os.getenv("api_token")
mail_id = os.getenv("mail_id")
print(mail_id)

auth = HTTPBasicAuth(mail_id, api_token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Issue created using python code.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    
    "issuetype": {
      "id": "10007"
    },
    
    "project": {
      "key": "DP"
    },
    
    "summary": "Issue_create_python",
    
    
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))