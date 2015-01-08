# simulate the mobile api client

import requests
import json
from sys import argv

script, user, password = argv

url = 'http://'+app.config['SERVER_URL']+'/api/people'
headers = {'Content-Type': 'application/json'}

filters = [dict(name='care_seeker', op='equals', val=1)]
# filters = [dict(name='care_giver', op='equals', val=1)]
params = dict(q=json.dumps(dict(filters=filters)))

response = requests.get(url, params=params, headers=headers, auth=(user, password))

if response.status_code == 200:
    print(response.json())
else:
    print response
