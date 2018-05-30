from check50 import *
import os

class FinalReflection(Checks):

    @check()
    def submitted(self):
        """You submitted 'Final Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("final_reflection") for filename in files):
            raise Error("File not found")
