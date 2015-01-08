#
# Usage: python test_send_message.py username password <message>
#
# Example: python test_send_message.py laurinda laurinda "help me please"
#

from sys import argv
from utils import send_message

script, username, password, message = argv
response = send_message(username, password, message)
# print(response.json())
