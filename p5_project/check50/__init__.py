from check50 import *
import os

class P5Project(Checks):

    @check()
    def submitted(self):
        """You submitted 'P5 Project'"""
        files = os.listdir()
#         if not any(filename.startswith("p5") for filename in files):
#             raise Error("File not found")
