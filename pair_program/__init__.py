import check50
import check50.c
import re


@check50.check()
def exists(self):
    """tempreflect.txt exists."""
    check50.exists("tempreflect.txt")
