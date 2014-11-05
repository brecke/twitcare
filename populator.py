from werkzeug import check_password_hash, generate_password_hash
from models import User, Message, UserFollow, db

SECRET_KEY = 'development key'

# miguel is a doctor
miguel = User('miguel', generate_password_hash('miguel'), 'me@miguellaginha.com', 1, 0)
print "user created: miguel (doctor)"

# joana is a nurse
joana = User('joana', generate_password_hash('joana'), 'heniswydryn@gmail.com', 1, 0)
print "user created: joana (nurse)"

# laurinda is a old lady that needs care
laurinda = User('laurinda', generate_password_hash('laurinda'), 'mail@example.com', 0, 1)
print "user created: laurinda (old lady)"

# save it
print "saving to database... "
db.session.add(laurinda)
db.session.add(miguel)
db.session.add(joana)
print "done."

# commit changes
print "committing changes... "
db.session.commit()
print "done."

# now that miguel and joana have id's, we can associate them
UserFollow(miguel, laurinda)
UserFollow(joana, laurinda)

# commit changes
print "committing changes... "
db.session.commit()
print "done."

# debug
for i in laurinda.followed_list:
    print "laurinda follows: ", i.followed

for i in laurinda.followed_by_list:
    print "laurinda is followed by: ", i.followed_by

# Laurinda asks for help!
tweet = Message(laurinda.id, "I need help, somebody help me!")

print "%s tweeted: %s " %(laurinda.username, tweet.text)
print "This tweet reached her followers: ", ", ".join(map(str, laurinda.followed_by_list))

db.session.add(tweet)
db.session.commit()

# print ", ".join(map(str, L))
