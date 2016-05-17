# pylint: disable=unused-variable,expression-not-assigned

from expecter import expect

from mctweetyface import models


def describe_get_name():

    def it_allow_any_word_as_an_override():
        expect(models.get_name("wordy")) == "Wordyy McWordyface"
