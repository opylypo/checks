from check50 import *
import os

class Tempreflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'Temperature Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("tempreflect") for filename in files):
            raise Error("File not found")
