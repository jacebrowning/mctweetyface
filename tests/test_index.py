# pylint: disable=unused-variable,expression-not-assigned

from expecter import expect


def describe_index():

    def describe_GET():

        def it_returns_random_name(client):
            response = client.get("/")

            expect(response.status_code) == 200
            expect(response.text).contains("face")
