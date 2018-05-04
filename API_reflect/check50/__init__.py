from check50 import *
import os

class APIreflect(Checks):

    @check()
    def submitted(self):
        """You submitted your 'Movie API Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("API_reflect") for filename in files):
            raise Error("File not found")
