from check50 import *
import os

class Caesarreflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'Caesar Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("caesarreflect") for filename in files):
            raise Error("File not found")
