from check50 import *
import os

class Breakout(Checks):

    @check()
    def submitted(self):
        """You submitted 'Breakout'"""
        files = os.listdir()
        if not any(filename.startswith("breakout") for filename in files):
            raise Error("File not found")
