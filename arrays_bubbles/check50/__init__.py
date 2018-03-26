from check50 import *
import os

class Arrays(Checks):

    @check()
    def submitted(self):
        """You submitted 'Arrays of Bubbles'"""
        files = os.listdir()
#         if not any(filename.startswith("sketch") for filename in files):
#             raise Error("File not found")
