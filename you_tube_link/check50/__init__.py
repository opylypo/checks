from check50 import *
import os

class YouTube(Checks):

    @check()
    def submitted(self):
        """You submitted 'YouTube Link'"""
        files = os.listdir()
        if not any(filename.startswith("you_tube_link") for filename in files):
            raise Error("File not found")
