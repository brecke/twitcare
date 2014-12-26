# -*- coding: utf-8 -*-

from werkzeug import check_password_hash, generate_password_hash
from models import User, Message, db

from authentication import SECRET_KEY

# id, username, password, e-mail, care-giver, care-seeker, full_name, current_location, avatar, care_type

# miguel is a doctor
miguel = User('miguel',
                'miguel',
                'me@miguellaginha.com',
                1,
                0,
                'Miguel Laginha',
                '37.136231, -8.015676',
                'http://www.womenshealthmag.com/files/images/0511-doctor-0460.jpg', '')

# joana is a nurse
joana = User('joana',
                'joana',
                'heniswydryn@gmail.com',
                1,
                0,
                'Joana Fernandes',
                '37.136231, -8.015676',
                'http://www.1stdoctor.com/wp-content/uploads/2013/11/woman_doctor_02.png', '')

# old woman face: http://slodive.com/wp-content/uploads/2013/04/short-hair-styles-for-older-women/cheerful-old-woman.jpg
# old man face: http://fc03.deviantart.net/fs71/i/2013/009/e/2/old_man_by_lash_upon_lash-d5j71hq.jpg

laurinda = User('laurinda', 'laurinda', 'quis@adipiscing.edu', 0, 1, 'Laurinda Silva', '37.136231, -8.015676', 'http://slodive.com/wp-content/uploads/2013/04/short-hair-styles-for-older-women/cheerful-old-woman.jpg', 'needs attention, mentally stable')
octavio = User('octavio', 'octavio', 'tellus@aliquam.net', 0, 1, 'Octavio Ferreira', '37.136231, -8.015676', 'http://fc03.deviantart.net/fs71/i/2013/009/e/2/old_man_by_lash_upon_lash-d5j71hq.jpg', 'phisically unstable')
filipe = User('filipe', 'filipe', 'cursus@luctus.com', 0, 1, 'Filipe Gomes', '37.136231, -8.015676', 'http://fc03.deviantart.net/fs71/i/2013/009/e/2/old_man_by_lash_upon_lash-d5j71hq.jpg', 'alzheimer\'s disease')
tomas = User('tomas', 'tomas', 'arcu@variusorci.edu', 0, 1, 'Tomas Luiz', '37.136231, -8.015676', 'http://fc03.deviantart.net/fs71/i/2013/009/e/2/old_man_by_lash_upon_lash-d5j71hq.jpg', 'healthy bloke, lives alone')
maria = User('maria', 'maria', 'vulputate@vulputate.edu', 0, 1, 'Maria Alice', '37.136231, -8.015676', 'http://slodive.com/wp-content/uploads/2013/04/short-hair-styles-for-older-women/cheerful-old-woman.jpg', 'parkinson\'s disease')
conceicao = User('conceicao', 'conceicao', 'magna.et.ipsum@sit.org', 0, 1, 'Maria da Conceicao', '37.136231, -8.015676', 'http://slodive.com/wp-content/uploads/2013/04/short-hair-styles-for-older-women/cheerful-old-woman.jpg', 'fragile who seeks care, lives alone')
rosa = User('rosa', 'rosa', 'scelerisque@sedleoCras.org', 0, 1, 'Rosa Maria', '37.136231, -8.015676', 'http://slodive.com/wp-content/uploads/2013/04/short-hair-styles-for-older-women/cheerful-old-woman.jpg', 'fit old lady, very active')

# save it
print "saving to database... "
db.session.add(laurinda)
db.session.add(octavio)
db.session.add(filipe)
db.session.add(tomas)
db.session.add(maria)
db.session.add(conceicao)
db.session.add(rosa)

db.session.add(miguel)
db.session.add(joana)
print "done."

# commit changes
print "committing changes... "
db.session.commit()
print "done."
