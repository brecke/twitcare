# simulate the mobile api client

import requests
import json

url = 'http://localhost:5000/api/people'
headers = {'Content-Type': 'application/json'}

filters = [dict(name='care_taker', op='equals', val=1)]
# filters = [dict(name='care_giver', op='equals', val=1)]
params = dict(q=json.dumps(dict(filters=filters)))

response = requests.get(url, params=params, headers=headers)

assert response.status_code == 200
print(response.json())