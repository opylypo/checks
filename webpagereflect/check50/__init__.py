from check50 import *

class Techexplore(Checks):

    @check()
    def submitted(self):
        """You submitted 'Scratch Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("scratchreflect") for filename in files):
            raise Error("File not found")
