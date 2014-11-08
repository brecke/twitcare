# Follow feed

import requests
import json
from datetime import datetime
from sys import argv

script, care_taker_id = argv

url = 'http://localhost:5000/api/subscription'
payload = {"care_taker_id": care_taker_id}
response = requests.delete(url, data=payload)

print(response)