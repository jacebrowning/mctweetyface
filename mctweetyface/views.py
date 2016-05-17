import logging

import bottle

from . import models, utils


app = bottle.app()

log = logging.getLogger(__name__)


@bottle.get("/")
def index():
    """Return a random name."""
    name = models.get_random_name()

    utils.tweet(name)

    return name
