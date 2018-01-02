from check50 import *

class Pset2(Checks):

    @check()
    def submitted(self):
        """You submitted 'PSET2 Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("pset2_reflection") for filename in files):
            raise Error("File not found")
