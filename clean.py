from stream_client import client

user_feed_1 = client.feed('user:1')
print dir(user_feed_1)
user_feed_1.remove_activity("82e1d736-66cd-11e4-8080-800137cff434")