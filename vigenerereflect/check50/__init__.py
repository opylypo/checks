from check50 import *
import os

class Vigenerereflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'Vigenere Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("vigenerereflect") for filename in files):
            raise Error("File not found")
