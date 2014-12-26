#
# Usage: python test_follow_feed care_seeker_username username password
#
# example: python test_follow_feed laurinda miguel <password_for_miguel>
#

import requests
import json
from datetime import datetime
from sys import argv

script, care_seeker_username, username, password = argv

url = 'http://localhost:5000/api/subscription'
payload = {"care_seeker_username": care_seeker_username}
response = requests.delete(url, data=payload, auth=(username, password))

print(response)
