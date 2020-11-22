import check50
import re

@check50.check()
def exists():
    """binary.py exists"""
    check50.exists("binary.py")
    
    
@check50.check(exists)
def finds2():
    """binary search finds 2"""
    check50.run("python3 binary.py").stdin("2").stdout("Found\n").exit(0)
    
