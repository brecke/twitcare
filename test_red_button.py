#
# Usage: python test_red_button.py username password <message>
#
# Example: python test_red_button.py laurinda laurinda "help me please"
#

import requests
import json
from datetime import datetime
from sys import argv

script, username, password, message = argv

now = str(datetime.now())
url = 'http://localhost:5000/api/messages'
payload = {"username": username, "text": message}
headers = {'content-type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers, auth=(username, password))

# assert response.status_code == 201
print(response.json())
