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
```

To debug:

```
heroku logs
```