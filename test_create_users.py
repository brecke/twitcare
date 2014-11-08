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

# Octavio
octavio = User('octavio', generate_password_hash('octavio'), 'email@example.com', 0, 1)
print "user created: octavio (old man)"

# save it
print "saving to database... "
db.session.add(laurinda)
db.session.add(octavio)

db.session.add(miguel)
db.session.add(joana)
print "done."

# commit changes
print "committing changes... "
db.session.commit()
print "done."