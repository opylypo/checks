from check50 import *
import os

class Searchreflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'Search Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("searchreflect") for filename in files):
            raise Error("File not found")
