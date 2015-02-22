#
# Usage: python test_follow_feed care_seeker_username username password
#
# example: python test_follow_feed laurinda miguel <password_for_miguel>
#

import requests
import json
from datetime import datetime
from sys import argv

script, id, username, password = argv

url = 'http://localhost:5000/api/unfollow/'+id
response = requests.put(url, auth=(username, password))

print(response)
