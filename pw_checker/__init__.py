import check50
import check50.c
import re

@check50.check()
def exists():
    """pwcheck.c exists."""
    check50.exists("pwcheck.c")

@check50.check(exists)
def compiles():
    """pwcheck.c compiles."""
    check50.c.compile("pwcheck.c", lcs50=True)

@check50.check(compiles)
def lowercaseonly():
    """Outputs Does Not Pass"""
    check50.run("./pwcheck").stdin("abcdefgh", prompt=False).stdout("Does Not Pass\n").exit(0)

@check50.check(compiles)
def uppercaseonly():
    """Outputs Does Not Pass"""
    check50.run("./pwcheck").stdin("ABCDEFGH", prompt=False).stdout("Does Not Pass\n").exit(0)

@check50.check(compiles)
def mixed_case():
    """Outputs Does Not Pass"""
    check50.run("./pwcheck").stdin("AbCcDd12", prompt=False).stdout("Does Not Pass\n").exit(0)

@check50.check(compiles)
def all_uppercase():
    """Outputs Passes"""
    check50.run("./pwcheck").stdin("AbCcDd1!", prompt=False).stdout("Passes\n").exit(0)

