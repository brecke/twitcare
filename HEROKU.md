# Instructions on how to deploy on heroku

```
heroku login
heroku create # only once
git push heroku master # if you're pushing master branch
git push heroku redesign:master # if you're pushing redesign branch
```

Then run the init or upgrade procedure:

```
heroku run init
heroku config:set GOOGLE_KEY=
heroku config:set API_KEY=
heroku config:set API_SECRET=
heroku config:set SERVER_URL=twitcare.herokuapp.com
```

To debug:

```
heroku logs
```