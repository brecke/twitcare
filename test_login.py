# Usage: python test_login.py username password

import requests
import json
from sys import argv
from server import SERVER_URL

script, user, password = argv

url = 'http://'+SERVER_URL+'/login'
r = requests.post(url, auth=(user, password))
