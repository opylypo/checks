from check50 import *
import os

class Movie(Checks):

    @check()
    def submitted(self):
        """You submitted your 'Movie API Program'"""
        files = os.listdir()
#         if not any(filename.startswith("movieAPI") for filename in files):
#             raise Error("File not found")
