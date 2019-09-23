import check50
import check50.c
import re


@check50.check()
def exists(self):
    """scratchreflect.txt exists."""
    check50.exists("scratchreflect.txt")
