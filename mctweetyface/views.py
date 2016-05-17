import logging

import bottle

from . import models

app = bottle.app()

log = logging.getLogger(__name__)


@bottle.get("/")
def index():
    """Return a random name."""
    return models.get_random_name()
