from check50 import *
import os

class Arrraysreflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'Arrays of Bubbles Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("arrays_reflect") for filename in files):
            raise Error("File not found")
