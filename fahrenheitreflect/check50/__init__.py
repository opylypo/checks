from check50 import *
import os

class Fahrenheitreflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'Fahrenheit Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("fahrenheitreflect") for filename in files):
            raise Error("File not found")
