from check50 import *


cclass Fahrenheit(Checks):

    @check()
    def exists(self):
        """fahrenheit.py exists"""
        self.require("fahrenheit.py")

    @check("exists")
    def test37(self):
        """37 degrees Celsius yields 98.6 degrees Fahrenheit"""
        self.spawn("python3 fahrenheit.py").stdin("37").stdout(number(98.6), "98.6\n").exit(0)

    @check("exists")
    def test0(self):
       """0 degrees Celsius yields 32.0 degrees Fahrenheit"""
        self.spawn("python3 fahrenheit.py").stdin("0").stdout(number(32.0), "32.0\n").exit(0)

    @check("exists")
    def test100(self):
        """100.00 degrees Celsius yields 212.0 degrees Fahrenheit"""
        self.spawn("python3 fahrenheit.py").stdin("100.00").stdout(number(212.0), "212.0\n").exit(0)
           
    @check("exists")
    def test100(self):
        """18.5 degrees Celsius yields 65.3 degrees Fahrenheit"""
        self.spawn("python3 fahrenheit.py").stdin("18.5").stdout(number(65.3), "65.3\n").exit(0)
