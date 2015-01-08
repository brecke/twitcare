import json
import requests
from datetime import datetime
from server import SERVER_URL

def send_message(username, password, message):
	now = str(datetime.now())
	url = 'http://'+SERVER_URL+'/api/messages'
	payload = {"username": username, "text": message}
	headers = {'content-type': 'application/json'}
	response = requests.post(url, data=json.dumps(payload), headers=headers, auth=(username, password))
	return response
	
def claim_message(message_id, username, password):
	url = 'http://'+SERVER_URL+'/api/claims/{}'.format(message_id)
	print "url: ", url
	headers = {'content-type': 'application/json'}
	response = requests.post(url, headers=headers, auth=(username, password))
	return response
	
def follow(care_seeker_username, username, password):
	url = 'http://'+SERVER_URL+'/api/subscription'
	payload = {"care_seeker_username": care_seeker_username}
	response = requests.post(url, data=payload, auth=(username, password))
	return response