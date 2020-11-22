import check50
import re

@check50.check()
def exists():
    """binary.py exists"""
    check50.exists("bubble.py")
    
    
@check50.check(exists)
def sorts():
    """sorts [1, 8, 4, 6, 0, 3, 5, 2, 7, 9]"""
    check50.run("python3 bubble.py").stdout("0 1 2 3 4 6 7 8 9 \n").exit(0)
