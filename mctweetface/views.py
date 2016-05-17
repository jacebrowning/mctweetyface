import logging

import bottle

app = bottle.app()

log = logging.getLogger(__name__)


@bottle.get("/")
def index():
    """Return a random name."""
    return "Boaty McBoatface"
