from check50 import *

class Webpagereflect(Checks):

    @check()
    def submitted(self):
        """You submitted 'Web Page Reflection'"""
        files = os.listdir()
        if not any(filename.startswith("webpagereflect") for filename in files):
            raise Error("File not found")
