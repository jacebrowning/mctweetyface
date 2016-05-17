# pylint: disable=unused-variable,expression-not-assigned

from expecter import expect
import bottle

from mctweetyface import views


def describe_index():

    def it_returns_a_string():
        expect(type(views.index())) == str

    def it_returns_random_results():
        bottle.request.query['update'] = False

        expect(views.index()) != views.index()
