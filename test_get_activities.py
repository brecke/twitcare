# simulate the mobile api client

import requests
import json
from sys import argv
from app import app

script, user, password = argv

url = 'http://'+app.config['SERVER_URL']+'/api/activities'
response = requests.get(url, auth=(user, password))

if response.status_code == 200:
	print(response.text)
else:
	print response
