from check50 import *
import os

class Friendsreflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'Friends Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("friendsreflect") for filename in files):
            raise Error("File not found")
