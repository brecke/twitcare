# Usage: python test_login.py username password

import requests
import json
from sys import argv
from app import app

script, user, password = argv

url = 'http://'+app.config['SERVER_URL']+'/login'
r = requests.post(url, auth=(user, password))
