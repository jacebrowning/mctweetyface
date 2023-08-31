# pylint: disable=unused-variable,expression-not-assigned,use-implicit-booleaness-not-comparison

from unittest.mock import patch, call

from expecter import expect

from mctweetyface import utils


def describe_tweet():

    @patch("mctweetyface.utils.api")
    @patch("mctweetyface.utils.auth.access_token", "my_token")
    def it_requires_a_matching_token_to_post(api):
        utils.tweet("Bad Message", token="invalid")
        expect(api.mock_calls) == []

        utils.tweet("Good Message", token="my_token")
        expect(api.mock_calls) == [call.update_status(status='Good Message')]
