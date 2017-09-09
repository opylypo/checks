from check50 import *


class Discomfort(Checks):

    @check()
    def submitted(self):
        """discomfort.txt exists"""
        pass

    @check()
    def at_least_50_words(self):
        """Assignment has at least 50 words"""
        with open("discomfort.txt") as f:
            word_count = len(f.read().split())
            if word_count < 50:
                raise Error("50 words required, only {} found.".format(word_count))
