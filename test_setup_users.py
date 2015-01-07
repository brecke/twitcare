# -*- coding: utf-8 -*-

from werkzeug import check_password_hash, generate_password_hash
from models import User, Message, db
from authentication import SECRET_KEY
from utils import follow
from utils import send_message

# delete all Users / Messages
print "About to drop all tables.."
db.drop_all()
db.session.commit()
print "Done."

print "Re-creating the model tables..."
db.create_all()
print "Done."

# id, username, password, e-mail, care-giver, care-seeker, full_name, current_location, avatar, care_type

# miguel is a doctor
miguel = User('miguel',
                'miguel',
                'me@miguellaginha.com',
                1,
                0,
                'Miguel Laginha',
                '40.205063, -8.407469',
                'http://www.womenshealthmag.com/files/images/0511-doctor-0460.jpg', '')

# joana is a nurse
joana = User('joana',
                'joana',
                'heniswydryn@gmail.com',
                1,
                0,
                'Joana Fernandes',
                '40.209053, -8.424377',
                'http://www.1stdoctor.com/wp-content/uploads/2013/11/woman_doctor_02.png', '')

# old woman face: http://slodive.com/wp-content/uploads/2013/04/short-hair-styles-for-older-women/cheerful-old-woman.jpg
# old man face: http://fc03.deviantart.net/fs71/i/2013/009/e/2/old_man_by_lash_upon_lash-d5j71hq.jpg

laurinda = User('laurinda', 'laurinda', 'quis@adipiscing.edu', 0, 1, 'Laurinda Silva', '40.180198, -8.396268', 'http://slodive.com/wp-content/uploads/2013/04/short-hair-styles-for-older-women/cheerful-old-woman.jpg', 'needs attention, mentally stable')
octavio = User('octavio', 'octavio', 'tellus@aliquam.net', 0, 1, 'Octavio Ferreira', '40.186378, -8.411020', 'http://fc03.deviantart.net/fs71/i/2013/009/e/2/old_man_by_lash_upon_lash-d5j71hq.jpg', 'phisically unstable')
filipe = User('filipe', 'filipe', 'cursus@luctus.com', 0, 1, 'Filipe Gomes', '40.191484, -8.419732', 'http://fc03.deviantart.net/fs71/i/2013/009/e/2/old_man_by_lash_upon_lash-d5j71hq.jpg', 'alzheimer\'s disease')
tomas = User('tomas', 'tomas', 'arcu@variusorci.edu', 0, 1, 'Tomas Luiz', '40.192148, -8.417468', 'http://fc03.deviantart.net/fs71/i/2013/009/e/2/old_man_by_lash_upon_lash-d5j71hq.jpg', 'healthy bloke, lives alone')
maria = User('maria', 'maria', 'vulputate@vulputate.edu', 0, 1, 'Maria Alice', '40.194787, -8.419356', 'http://slodive.com/wp-content/uploads/2013/04/short-hair-styles-for-older-women/cheerful-old-woman.jpg', 'parkinson\'s disease')
conceicao = User('conceicao', 'conceicao', 'magna.et.ipsum@sit.org', 0, 1, 'Maria da Conceicao', '40.200507, -8.407308', 'http://slodive.com/wp-content/uploads/2013/04/short-hair-styles-for-older-women/cheerful-old-woman.jpg', 'fragile who seeks care, lives alone')
rosa = User('rosa', 'rosa', 'scelerisque@sedleoCras.org', 0, 1, 'Rosa Maria', '40.205063, -8.407469', 'http://slodive.com/wp-content/uploads/2013/04/short-hair-styles-for-older-women/cheerful-old-woman.jpg', 'fit old lady, very active')

# save it
print "Saving dummy users to database... "
db.session.add(laurinda)
db.session.add(octavio)
db.session.add(filipe)
db.session.add(tomas)
db.session.add(maria)
db.session.add(conceicao)
db.session.add(rosa)

db.session.add(miguel)
db.session.add(joana)

db.session.commit()
print "Done."


print "Now creating some follower/followed relationships..."
# make miguel follow the men
# python test_follow_feed.py care_seeker care_giver password_for_care_giver

follow('octavio', 'miguel', 'miguel')
follow('filipe', 'miguel', 'miguel')
follow('tomas', 'miguel', 'miguel')
 
# make joana follow the women
# python test_follow_feed.py care_seeker care_giver password_for_care_giver
follow('laurinda', 'joana', 'joana')
follow('maria', 'joana', 'joana')
follow('conceicao', 'joana', 'joana')
follow('rosa', 'joana', 'joana')
 
# send some alert messages
send_message('octavio', 'octavio', 'I fell from my bed, I need help')
send_message('maria', 'maria', 'I cant eat on my own, help me please')
send_message('rosa', 'rosa', 'I want to do some exercise, will somebody assist me?')
print "Done."

# commit changes
print "Finally committing changes... "
db.session.commit()
print "All done."
