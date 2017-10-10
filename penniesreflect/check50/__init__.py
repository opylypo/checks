from check50 import *
import os

class Penniesreflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'Pennies Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("penniesreflect") for filename in files):
            raise Error("File not found")
