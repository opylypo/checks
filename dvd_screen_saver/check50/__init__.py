from check50 import *
import os

class DVDScreenSaverChecks):

    @check()
    def submitted(self):
        """You submitted 'DVD Screen Saver'"""
        files = os.listdir()
#         if not any(filename.startswith("skittles") for filename in files):
#             raise Error("File not found")
