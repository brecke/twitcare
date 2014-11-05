# simulate the UserFollow POST to send tweet

import requests
import json
from datetime import datetime

now = str(datetime.now())
url = 'http://localhost:5000/api/messages'
# payload = {"author_id": 1, "text": "help!", "pub_date": now}
payload = {"author_id": 1, "text": "help!"}
print payload
headers = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)

print r.url
print r.text
