from check50 import *
import os

class Dvdreflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'DVD Screen Saver Reflection'"""
        files = os.listdir()
