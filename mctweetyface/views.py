import logging

import bottle

from . import models, utils


app = bottle.app()

log = logging.getLogger(__name__)


@bottle.get("/")
def index():
    """Return a name."""
    word = bottle.request.query.get('name')

    name = models.get_name(word)

    utils.tweet(name, token=bottle.request.headers.get('Authorization'))

    return name
