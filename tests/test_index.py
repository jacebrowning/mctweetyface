# pylint: disable=unused-variable,expression-not-assigned

from expecter import expect


def describe_index():

    def describe_GET():

        def it_returns_name(client):
            response = client.get("/?update=true")

            expect(response.status_code) == 200
            expect(response.text).contains("face")

        def it_returns_given_name(client):
            response = client.get("/?name=toast")

            expect(response.status_code) == 200
            expect(response.text).contains("Toasty McToastface")
