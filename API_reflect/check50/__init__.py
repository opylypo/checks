from check50 import *
import os

class Marioreflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'Mario Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("marioreflect") for filename in files):
            raise Error("File not found")
