from check50 import *
import os

class P5SpaceShip(Checks):

    @check()
    def submitted(self):
        """You submitted 'p5 spaceship warmup'"""
        files = os.listdir()
#         if not any(filename.startswith("skittles") for filename in files):
#             raise Error("File not found")
