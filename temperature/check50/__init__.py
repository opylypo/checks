from check50 import *
import os

class Temperature(Checks):

    @check()
    def submitted(self):
        """You submitted 'Temperature'"""
        files = os.listdir()
#         if not any(filename.startswith("temp") for filename in files):
#             raise Error("File not found")
