# Readme

## Setup

Clone this repository

```
git clone https://github.com/brecke/twitcare.git
```

Install requirements

```
pip install -r requirements.txt
```

Now you can run:

```
python main.py
```

Check out http://localhost:5000/api/user for instance.

You may also use gunicorn as an alternative:

```
gunicorn --log-file - main:app
```

## Stream flow

There are two types of feeds being used: flat feeds - one for each care seeker - and notification feeds - one for each care giver.
The flat feed is called 'user' as in 'user:1', if he id 1 corresponds to a care seeker. The notification fee is called 'notification' as in 'notification:8', assuming 8 is the id of a care giver in the database.

The care givers feeds follow care seekers feeds. 

From dummy data, one establishes that:

- miguel (care giver) follows the male care seekers
- joana (care giver) follows the female care seekers

Code for this:

```
 # create users
python test_create_users.py

 # make miguel follow the men
 # python test_follow_feed.py care_seeker care_giver password_for_care_giver
python test_follow_feed.py octavio miguel miguel
python test_follow_feed.py octavio miguel miguel
python test_follow_feed.py octavio miguel miguel

 # make joana follow the women
 # python test_follow_feed.py care_seeker care_giver password_for_care_giver
python test_follow_feed.py laurinda joana joana
python test_follow_feed.py maria joana joana
python test_follow_feed.py conceicao joana joana
python test_follow_feed.py rosa joana joana

 # send some alert messages
python test_red_button.py octavio octavio 'I fell from my bed, I need help'
python test_red_button.py maria maria 'I cant eat on my own, help me please'
python test_red_button.py rosa rosa 'I want to do some exercise, will somebody assist me?'
```