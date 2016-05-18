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


def tweet(message, token=None):
    """Post a message on Twitter using the loaded credentials."""
    if not auth.access_token:
        log.warning("Twitter access token not provided")
        return

    if token != auth.access_token:
        log.error("Twitter access token is invalid")
        return

    api.update_status(status=message)
