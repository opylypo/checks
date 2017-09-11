from check50 import *

class Discomfort(Checks):

    @check()
    def submitted(self):
        """You submitted 'What is my discomfort'"""
        files = os.listdir()
        if not any(filename.startswith("discomfort") for filename in files):
            raise Error("File not found")