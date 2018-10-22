from check50 import *


class Glocal(Checks):

    @check()
    def exists(self):
        """glocal.c exists"""
        self.require("glocal.c")

    @check("exists")
    def compiles(self):
        """glocal.c compiles"""
        self.spawn("clang -std=c11 -o glocal glocal.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test1(self):
        """input of 1 yields output of 6"""
        self.spawn("./glocal").stdin("1").stdout(number(6), "6\n").exit(0)

    @check("compiles")
    def test0(self):
        """input of 0 yields output of 5"""
        self.spawn("./glocal").stdin("0").stdout(number(5), "5\n").exit(0)

    @check("compiles")
    def test100(self):
        """input of 100 yields output of 105"""
        self.spawn("./glocal").stdin("100").stdout(number(105), "105\n").exit(0)

    @check("compiles")
    def test_reject_foo(self):
        """rejects a non-numeric input of "foo" """
        self.spawn("./glocal").stdin("foo").reject()

    @check("compiles")
    def test_reject_empty_string(self):
        """rejects a non-numeric input of "" """
        self.spawn("./glocal").stdin("").reject()



def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
