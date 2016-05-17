import random
from pathlib import Path

_NOUNS = None


def get_random_noun():
    """Load a random noun from the dictionary."""
    global _NOUNS

    if not _NOUNS:
        with Path(__file__).parent.joinpath("nounlist.txt").open() as f:
            _NOUNS = f.read().splitlines()

    return random.choice(_NOUNS)


def get_name(target=None):
    """Generate a name from a given target, or use a random noun."""
    noun = target

    if not target:
        while any(_rejected(noun)):
            noun = get_random_noun()

    return "{0}y Mc{0}face".format(noun.capitalize())


def _rejected(noun):
    yield not noun
    yield noun.endswith('y')
    yield noun.endswith('ing')
    yield ' ' in noun
    yield '-' in noun
    yield len(noun) > 8
