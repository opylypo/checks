from check50 import *

class Pset1reflection(Checks):

    @check()
    def submitted(self):
        """You submitted 'PSET1 Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("pset1_reflection") for filename in files):
            raise Error("File not found")
