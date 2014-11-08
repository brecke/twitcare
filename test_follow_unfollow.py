import requests
import json
from datetime import datetime

headers = {'Content-Type': 'application/json'}

def find_user_by_followed_id(user_id):
    """docstring for do_request"""

    # print laurinda followers
    url = 'http://127.0.0.1:5000/api/followers'
    filters = [dict(name='followed_id', op='equals', val=user_id)]
    params = dict(q=json.dumps(dict(filters=filters)))
    response = requests.get(url, params=params, headers=headers)
    # print(response.json())
    return response

response = find_user_by_followed_id(1) # laurinda
print "There are %s followers right now:" % response.json().get('num_results')

# unfollow one of them
url = 'http://127.0.0.1:5000/api/followers/1'
response = requests.delete(url, headers=headers)

do_request()

url = 'http://127.0.0.1:5000/api/followers/'
response.get(url, headers=headers, params)
payload = {"followed_by": miguel.id, "followed": laurinda.id}
response = requests.post(url, headers=headers, data=json.dumps(payload))

do_request()