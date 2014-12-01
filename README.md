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
