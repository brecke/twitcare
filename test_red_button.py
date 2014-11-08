# simulate the UserFollow POST to send tweet

import requests
import json
from datetime import datetime
from sys import argv

script, author_id, message = argv

now = str(datetime.now())
url = 'http://localhost:5000/api/messages'
payload = {"author_id": author_id, "text": message}
headers = {'content-type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers)

assert response.status_code == 201
print(response.json())
