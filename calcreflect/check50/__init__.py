from check50 import *
import os

class Greedyreflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'Greedy Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("greedyreflect") for filename in files):
            raise Error("File not found")
