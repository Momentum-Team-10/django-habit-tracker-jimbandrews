# Project Notes

## Heroku Setup

- had to do a few extra steps to avoid an error with collectstatic  
    1. `heroku config:set DISABLE_COLLECTSTATIC=1`
    2. `git push heroku main`
    3. `python manage.py collectstatic --noinput`
    4. `heroku config:unset DISABLE_COLLECTSTATIC`

- took a screenshot of my previous error during deployment
- FOR LATER: look into what collectstaticdoes in Django

- for InconsistentMigrationHistory -- just run `heroku pg:reset DATABASE_URL` in the command line
## Product Requirements

1. registration and login  
    - need to implement django-registration-redux

2. what users should create
    - start with User and Habit models
    - used django [validator](https://docs.djangoproject.com/en/3.2/ref/validators/#minvaluevalidator) to put lower bound on Habit target (but this might be incorrect)
    - added DailyRecord model

