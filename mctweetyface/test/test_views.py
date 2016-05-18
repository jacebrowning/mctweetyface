# pylint: disable=unused-variable,expression-not-assigned,unused-argument

import pytest
from expecter import expect
import bottle

from mctweetyface import views


def describe_index():

    @pytest.fixture
    def query():
        bottle.request.query['name'] = None  # pylint: disable=unsubscriptable-object
        return bottle.request.query

    def it_returns_random_results(query):
        expect(views.index()) != views.index()

    def it_accepts_a_custom_base(query):
        query['name'] = "foobar"
        expect(views.index()) == "Foobary McFoobarface"
