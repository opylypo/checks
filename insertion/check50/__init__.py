from check50 import *


class Insertion(Checks):

    @check()
    def exists(self):
        """insertion.c exists."""
        self.require("insertion.c")

    @check("exists")
    def compiles(self):
        """insertion.c compiles."""
        self.spawn("clang -std=c11 -o insertion insertion.c -lcs50 -lm").exit(0)

    @check("compiles")
    def sorts(self):
        """sorts {50, 19, 64, 7, 108, 42, 82}"""
        self.spawn("./insertion").stdout("7 19 42 50 64 82 108\n").exit(0)
