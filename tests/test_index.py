# pylint: disable=unused-variable,expression-not-assigned

from expecter import expect


def describe_index():

    def describe_GET():

        def it_returns_a_name(client):
            response = client.get("/")

            expect(response.status_code) == 200
            expect(response.text).contains("face")

        def it_uses_a_specified_root(client):
            response = client.get("/?name=toast")

            expect(response.status_code) == 200
            expect(response.text).contains("Toasty McToastface")
