from app import app
import json
import pusher

def send_push(activity):
	
	p = pusher.Pusher(
  		app_id=app.config['PUSHER_APP_ID'],
  		key=app.config['PUSHER_KEY'],
  		secret=app.config['PUSHER_SECRET']
	)
	
	p['tweetcare'].trigger('help_request', json.dumps(activity))
	
	