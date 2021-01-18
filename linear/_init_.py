import check50
import re

@check50.check()
def exists():
    """linear.py exists"""
    check50.exists("linear.c")
    
    
@check50.check(exists)
def finds2():
    """linear search finds 7"""
    check50.run("python3 linear.py").stdin("7").stdout("Bingo! Found 7!\n").exit(0)
    

@check50.check(exists)
def finds14():
    """binary search finds 26"""
    check50.run("python3 linear.py").stdin("26").stdout("Bingo! Found 26!\n").exit(0)   
    
    
@check50.check(exists)
def finds14():
    """binary search does not find 70"""
    check50.run("python3 linear.py").stdin("70").stdout("Sorry better luck next time!\n").exit(0)   
