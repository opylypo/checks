from check50 import *
import os

class FinalProject(Checks):

    @check()
    def submitted(self):
        """You submitted 'Final Project Link'"""
        files = os.listdir()
        if not any(filename.startswith("final_project") for filename in files):
            raise Error("File not found")
