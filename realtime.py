from app import app
import json
import pusher

def send_push(activity, follower_id):
	
	p = pusher.Pusher(
  		app_id=app.config['PUSHER_APP_ID'],
  		key=app.config['PUSHER_KEY'],
  		secret=app.config['PUSHER_SECRET']
	)
	
	print "pushing to channel tweetcare:{}".format(follower_id)

	p["tweetcare:{}".format(follower_id)].trigger('help_request', json.dumps(activity))
	
	