from check50 import *
import os

class Exploretwo(Checks):

    @check()
    def submitted(self):
        """You submitted 'Second Practice Explore'"""
        files = os.listdir()
        if not any(filename.startswith("exploretwo") for filename in files):
            raise Error("File not found")
