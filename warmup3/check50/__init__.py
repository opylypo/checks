from check50 import *


class Sigma(Checks):

    @check()
    def exists(self):
        """sigma.c exists"""
        self.require("sigma.c")

    @check("exists")
    def compiles(self):
        """sigma.c compiles"""
        self.spawn("clang -std=c11 -o calc sigma.c -lcs50 -lm").exit(0)
        
    @check("compiles")
    def test_handles_1_argument(self):
        """sigma handles 10"""
        self.spawn("./sigma 10").stdout("10\n").exit(0)

    @check("compiles")
    def test_handles_2_arguments(self):
        """sigma handles 3 + 4"""
        self.spawn("./sigma 3 4").stdout(number("7"), "7\n").exit(0)

    @check("compiles")
    def test_handles_4_arguments(self):
        """sigma handles 1 + 2 + 3 + 4"""
        self.spawn("./sigma 1 2 3 4").stdout(number("10"), "10\n").exit(0)

    @check("compiles")
    def test_handles_0_arguments(self):
        """calculator handles no arguments"""
        self.spawn("./sigma").stdout(number(0), "0\n").exit(0)


def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
