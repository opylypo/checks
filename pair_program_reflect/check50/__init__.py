from check50 import *

class Pairreflection(Checks):

    @check()
    def submitted(self):
        """You submitted 'Pair Programming Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("pair_program_reflect") for filename in files):
            raise Error("File not found")
