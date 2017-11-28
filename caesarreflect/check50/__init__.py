from check50 import *
import os

class Isbnreflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'ISBN Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("isbnreflect") for filename in files):
            raise Error("File not found")
