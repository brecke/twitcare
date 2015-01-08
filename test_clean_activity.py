from models import User
from stream_client import client

users = User.query.all()
for user in users:
	if user.care_giver == 1:
		feed = client.feed('notification:{}'.format(user.id))
		
		followed_feeds = feed.following()
		for followed_feed in followed_feeds.get('results'):
			target = followed_feed.get('target_id')
			
			param1 = target.split(':')[0]
			param2 = target.split(':')[-1]
			print "Unfollowing ", target
			feed.unfollow(target) 
			
	elif user.care_seeker == 1:
		feed = client.feed('user:{}'.format(user.id))
	
	activities = feed.get()
	# print activities
	for activity in activities.get('results'):
		print "Erasing...", activity.get('id')
		feed.remove_activity(activity.get('id'))
		
# print dir(user_feed_1)
# user_feed_1.remove_activity("82e1d736-66cd-11e4-8080-800137cff434")