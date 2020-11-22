import check50
import re

@check50.check()
def exists():
    """binary.py exists"""
    check50.exists("bubble.py")
    
    
@check50.check(exists)
def sorts():
    """sorts {64, 34, 25, 12, 22, 11, 90}"""
    check50.run("python3 bubble.py").stdout("11 12 22 25 34 64 90 \n").exit(0)
