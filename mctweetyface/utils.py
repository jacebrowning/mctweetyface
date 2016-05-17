import os
import logging

import tweepy


log = logging.getLogger(__name__)

auth = tweepy.OAuthHandler(
    os.getenv('TWITTER_API_KEY'),
    os.getenv('TWITTER_API_SECRET'),
)
auth.set_access_token(
    os.getenv('TWITTER_ACCESS_TOKEN'),
    os.getenv('TWITTER_ACCESS_SECRET'),
)
api = tweepy.API(auth)


def tweet(message):
    """Post a message on Twitter using the loaded credentials."""
    try:
        api.update_status(status=message)
    except tweepy.error.TweepError as exception:
        log.warning(exception)
