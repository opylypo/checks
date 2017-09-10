from check50 import *


class Discomfort(Checks):

    @check()
    def submitted(self):
        """discomfort.txt exists"""
        pass

    @check()
    def at_least_200_words(self):
        """Assignment has approx 300 to 500 words"""
        with open("discomfort.txt") as f:
            word_count = len(f.read().split())
            if word_count < 200:
                raise Error("300 to 500 words required, only {} found.".format(word_count))
