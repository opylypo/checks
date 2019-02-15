from check50 import *

class Pset7(Checks):

    @check()
    def submitted(self):
        """You submitted 'PSET7 Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("pset7_reflection") for filename in files):
            raise Error("File not found")
