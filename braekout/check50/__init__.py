from check50 import *
import os

class Pong(Checks):

    @check()
    def submitted(self):
        """You submitted 'Pong'"""
        files = os.listdir()
        if not any(filename.startswith("pong") for filename in files):
            raise Error("File not found")
