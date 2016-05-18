import random
from pathlib import Path
import logging


_NOUNS = None

log = logging.getLogger(__name__)


def get_random_word():
    """Load a random noun from the dictionary."""
    global _NOUNS

    if not _NOUNS:
        with Path(__file__).parent.joinpath("nounlist.txt").open() as f:
            _NOUNS = f.read().splitlines()

    return random.choice(_NOUNS)


def get_name(word=None):
    """Generate a name from a given target, or use a random noun."""
    if word:
        log.info("Specified base word: %s", word)
    else:
        while any(_rejected(word)):
            word = get_random_word()
        log.info("Random base word: %s", word)

    return "{0}y Mc{0}face".format(word.capitalize())


def _rejected(word):
    yield not word
    yield word.endswith('y')
    yield word.endswith('ing')
    yield ' ' in word
    yield '-' in word
    yield len(word) > 8
