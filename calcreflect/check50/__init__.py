from check50 import *
import os

class Calcreflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'Calc Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("calcreflect") for filename in files):
            raise Error("File not found")
