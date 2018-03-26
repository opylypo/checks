from check50 import *
import os

class Bubblesreflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'Bubbles Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("bubbles_reflect") for filename in files):
            raise Error("File not found")
