from check50 import *
import os

class Initialsreflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'Initials Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("initialsreflect") for filename in files):
            raise Error("File not found")
