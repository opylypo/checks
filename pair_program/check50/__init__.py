from check50 import *
import os

class Pairprogram(Checks):

    @check()
    def submitted(self):
        """You submitted 'Pair Programming Problem'"""
        files = os.listdir()
#         if not any(filename.startswith("skittles") for filename in files):
#             raise Error("File not found")
