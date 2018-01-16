from check50 import *

class Pset3(Checks):

    @check()
    def submitted(self):
        """You submitted 'PSET3 Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("pset3_reflection") for filename in files):
            raise Error("File not found")
