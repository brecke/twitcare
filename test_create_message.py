from models import User, Message, db

# laurinda
id = 1

# octavio
id = 2

# Laurinda asks for help!
tweet = Message(id, "I need help, somebody help me!")
print "User_id %s tweeted: %s " %(id, tweet.text)

db.session.add(tweet)
db.session.commit()
