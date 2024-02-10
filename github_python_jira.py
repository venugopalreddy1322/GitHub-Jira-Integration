# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from flask import Flask
# Creating a flask application instance
app = Flask(__name__)
# define a route that handles POST requests
@app.route('/createjira', methods=['POST'])  # decorator, which runs before main()
def create_jira():
    # Jira account URL
    url = "https://venu-devops.atlassian.net/rest/api/3/issue"
    # Passing api_token and mail_id as environment variables using export command in command-line
    api_token = os.getenv("api_token")
    mail_id = os.getenv("mail_id")
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
                "text": "Issue created using python code by GitHub.",
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
        "id": "10007" #story
        },
        
        "project": {
        "key": "DP"
        },
        
        "summary": "create_issue_by_gitHub_action",
        
        
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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # flask runs on port 5000 can be changed if needed