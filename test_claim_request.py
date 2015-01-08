#
# Usage: python test_claim_request.py message_id username password <message>
#
# Example: python test_claim_request.py 14 miguel miguel
#

from sys import argv
from utils import claim_message

script, message_id, username, password = argv
response = claim_message(message_id, username, password)
# print(response.json())
