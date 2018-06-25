from __future__ import absolute_import, unicode_literals
from .celery import app

try:
    import json
except ImportError:
    import simplejson as json

@app.task
def twt(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET):
    # Import the necessary methods from "twitter" library
    import twitter

    oauth = twitter.OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    # Initiate the connection to Twitter User API
    twitter = twitter.Twitter(auth=oauth)

    # Get a sample of the public data following through Twitter
    alltweets = twitter.statuses.user_timeline(screen_name="iamchap24")
    d = []

    for tweet in alltweets:
        d.append(tweet['text'])

    return d
