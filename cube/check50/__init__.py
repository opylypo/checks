import re

from check50 import *

class Cube(Checks):

    @check()
    def exists(self):
        """cube.py exists"""
        self.require("cube.py")

    @check("exists")
    def test041(self):
        """input of 1 yields output of 1"""
        self.spawn("python3 cube.py").stdin("1").stdout("1\n").exit(0)

    @check("exists")
    def test001(self):
        """input of 2 yields output of 8"""
        self.spawn("python3 cube.py").stdin("2").stdout("8\n").exit(0)

    @check("exists")
    def test015(self):
        """input of 10 yields output of 1000"""
        self.spawn("python3 cube.py").stdin("10").stdout("1000\n").exit(0)


    @check("exists")
    def test_reject_negative(self):
        """rejects a non-integer input like 1.2"""
        self.spawn("python3 cube.py").stdin("1.2").reject()

    @check("exists")
    def test_reject_foo(self):
        """rejects a non-numeric input of "foo" """
        self.spawn("python3 cube.py").stdin("foo").reject()

    @check("exists")
    def test_reject_empty(self):
        """rejects a non-numeric input of "" """
        self.spawn("python3 cube.py").stdin("").reject()


