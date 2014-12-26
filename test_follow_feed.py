#
# Usage: python test_follow_feed care_seeker_username username password
#
# example: python test_follow_feed laurinda miguel <password_for_miguel>
#

import requests
import json
from datetime import datetime
from sys import argv
from server import SERVER_URL

script, care_seeker_username, username, password = argv

url = 'http://'+SERVER_URL+'/api/subscription'
payload = {"care_seeker_username": care_seeker_username}
response = requests.post(url, data=payload, auth=(username, password))

print(response)
