import requests
import json
from sys import argv

script, user, password = argv

url = 'http://localhost:5000/login'
r = requests.post(url, auth=(user, password))
print r
