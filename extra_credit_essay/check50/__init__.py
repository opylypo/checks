from check50 import *
import os

class Extracreditessay(Checks):

    @check()
    def submitted(self):
        """You submitted 'Extra Credit Essay'"""
        files = os.listdir()
        if not any(filename.startswith("extra_credit_essay") for filename in files):
            raise Error("File not found")
