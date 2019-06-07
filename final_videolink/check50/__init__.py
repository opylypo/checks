from check50 import *
import os

class FinalVideo(Checks):

    @check()
    def submitted(self):
        """You submitted 'Final Video Link'"""
        files = os.listdir()
        if not any(filename.startswith("final_project") for filename in files):
            raise Error("File not found")
