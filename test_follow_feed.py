#
# Usage: python test_follow_feed care_taker_username username password
#
# example: python test_follow_feed laurinda miguel <password_for_miguel>
#

import requests
import json
from datetime import datetime
from sys import argv

script, care_taker_username, username, password = argv

url = 'http://localhost:5000/api/subscription'
payload = {"care_taker_username": care_taker_username}
response = requests.post(url, data=payload, auth=(username, password))

print(response)
