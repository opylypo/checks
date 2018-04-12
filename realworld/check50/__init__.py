from check50 import *
import os

class Extracreditessay(Checks):

    @check()
    def submitted(self):
        """You submitted 'Real World Essay'"""
        files = os.listdir()
        if not any(filename.startswith("realworld") for filename in files):
            raise Error("File not found")
