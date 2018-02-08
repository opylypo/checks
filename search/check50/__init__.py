from check50 import *
import os

class Search(Checks):

    @check()
    def submitted(self):
        """You submitted 'Search Engine'"""
        files = os.listdir()
#         if not any(filename.startswith("friendsreflect") for filename in files):
#             raise Error("File not found")
