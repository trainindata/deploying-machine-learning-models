#!/usr/bin/env bash
export IS_DEBUG=${DEBUG:-false}

# We run gunicord to start our Flask application
# This is similar to what we have in the Procfile for Heroku setup
exec gunicorn --bind 0.0.0.0:5000 --access-logfile - --error-logfile - run:application
