from check50 import *

class Techexplore(Checks):

    @check()
    def submitted(self):
        """You submitted 'Practice Explore Task'"""
        files = os.listdir()
        if not any(filename.startswith("tech") for filename in files):
            raise Error("File not found")