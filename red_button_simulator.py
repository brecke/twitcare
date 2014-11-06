# simulate the UserFollow POST to send tweet

import requests
import json
from datetime import datetime

now = str(datetime.now())
url = 'http://localhost:5000/api/messages'
# payload = {"author_id": 1, "text": "help!", "pub_date": now}
payload = {"author_id": 1, "text": "help!"}
# print payload
headers = {'content-type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers)

assert response.status_code == 201
print(response.json())

# debug
# print r.url
# print r.text
