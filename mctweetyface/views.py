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

    if bottle.request.query.get('update'):
        utils.tweet(name)

    return name
