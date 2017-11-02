from check50 import *

class Techexplore(Checks):

    @check()
    def submitted(self):
        """You submitted 'Second Scratch Project'"""
        files = os.listdir()
        if not any(filename.startswith("scratch") for filename in files):
            raise Error("File not found")
