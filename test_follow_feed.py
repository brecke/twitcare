#
# Usage: python test_follow_feed care_seeker_username username password
#
# example: python test_follow_feed laurinda miguel <password_for_miguel>
#

from sys import argv
from utils import follow

script, care_seeker_username, username, password = argv
response = follow(care_seeker_username, username, password)
print(response)