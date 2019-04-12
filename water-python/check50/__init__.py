import re

from check50 import *


class Water(Checks):

    @check()
    def exists(self):
        """water.py exists"""
        self.require("water.py")

    @check("exists")
    def test1(self):
        """1 minute equals 12 bottles."""
        self.spawn("python water.py").stdin("1").stdout(bottles(12), "12\n")
        
    @check("exists")
    def test2(self):
        """2 minute equals 24 bottles."""
        self.spawn("python water.py").stdin("2").stdout(bottles(24), "24\n")
        
    @check("exists")
    def test5(self):
        """5 minute equals 60 bottles."""
        self.spawn("python water.py").stdin("5").stdout(bottles(60), "60\n").exit(0)
        
    @check("exists")
    def test10(self):
        """10 minute equals 120 bottles."""
        self.spawn("python water.py").stdin("10").stdout(bottles(120), "120\n").exit(0)    

    @check("exists")
    def test_reject_foo(self):
        """rejects a non-numeric input of "foo" """
        self.spawn("python3 water.py").stdin("foo").reject()
        
    @check("exists")
    def test_reject_empty(self):
        """rejects "" minutes"""
        self.spawn("python3 water.py").stdin("").reject()
        
    @check("exists")
    def test_reject_123abc(self):
        """rejects "123abc" minutes"""
        self.spawn("python water.py").stdin("123abc").reject()


        
        


def bottles(num):
    return "(^|[^\d]){}[^\d]".format(num)
