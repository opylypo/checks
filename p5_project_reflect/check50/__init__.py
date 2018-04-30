from check50 import *
import os

class P5ProjectReflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'P5 Project Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("p5_project_reflect") for filename in files):
            raise Error("File not found")
