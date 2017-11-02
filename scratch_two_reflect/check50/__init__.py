from check50 import *

class Techexplore(Checks):

    @check()
    def submitted(self):
        """You submitted 'Second Scratch Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("scratch_two_reflect") for filename in files):
            raise Error("File not found")
