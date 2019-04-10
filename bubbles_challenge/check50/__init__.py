from check50 import *
import os

class Bubbles(Checks):

    @check()
    def submitted(self):
        """You submitted 'Bubbles Challenge'"""
        files = os.listdir()
        if not any(filename.startswith("sketch") for filename in files):
            raise Error("File not found")
