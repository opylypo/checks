from check50 import *


class Insert(Checks):

    @check()
    def exists(self):
        """insert.c exists"""
        self.require("glocal.c")

    @check("exists")
    def compiles(self):
        """insert.c compiles"""
        self.spawn("clang -std=c11 -o insert insert.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test1(self):
        """input of 10.2 yields output of -3.5 5.6 7.0 8.2 9.7 10.2 18.3"""
        self.spawn("./glocal").stdin("10.2").stdout("-3.5 5.6 7.0 8.2 9.7 10.2 18.3 \n").exit(0)

    @check("compiles")
    def test0(self):
        """input of 23.1 yields output of -3.5 5.6 7.0 8.2 9.7 18.3 23.1"""
        self.spawn("./glocal").stdin("23.1").stdout("-3.5 5.6 7.0 8.2 9.7 18.3 23.1 \n").exit(0)

    @check("compiles")
    def test100(self):
        """input of 0 yields output of -3.5 0.0 5.6 7.0 8.2 9.7 18.3"""
        self.spawn("./glocal").stdin("0").stdout("-3.5 0.0 5.6 7.0 8.2 9.7 18.3 \n").exit(0)
           
   @check("compiles")
    def test100(self):
        """input of -5.8 yields output of -5.8 -3.5 5.6 7.0 8.2 9.7 18.3"""
        self.spawn("./glocal").stdin("-5.8").stdout("-5.8 -3.5 5.6 7.0 8.2 9.7 18.3 \n").exit(0)

    

