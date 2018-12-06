from check50 import *

class Pset6(Checks):

    @check()
    def submitted(self):
        """You submitted 'PSET6 Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("pset6_reflection") for filename in files):
            raise Error("File not found")
