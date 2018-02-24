from check50 import *

class Pset4(Checks):

    @check()
    def submitted(self):
        """You submitted 'PSET4 Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("pset4_reflection") for filename in files):
            raise Error("File not found")
