#
# Usage: python test_follow_feed care_seeker_username username password
#
# example: python test_follow_feed laurinda miguel <password_for_miguel>
#

from sys import argv
from utils import following

script, username, password = argv
response = following(username, password)
print(response)