import logging

import bottle

from . import models, utils


app = bottle.app()

log = logging.getLogger(__name__)


@bottle.get("/")
def index():
    """Return a name."""
    target = bottle.request.query.get('name')
    name = models.get_name(target)

    utils.tweet(name, token=bottle.request.headers.get('Authorization'))

    return name
