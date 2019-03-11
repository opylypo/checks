from check50 import *
import os

class Gridchallenge(Checks):

    @check()
    def submitted(self):
        """You submitted 'Grid Challenge'"""
        files = os.listdir()

