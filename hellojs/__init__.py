import check50
import check50.c
import re

@check50.check()
def exists():
    """hello.js exists."""
    check50.exists("hello.js")

@check50.check(compiles)
def prints_hello():
    """prints "hello, world\\n" """
    from re import match

    expected = "[Hh]ello, world!?\n"
    actual = check50.run("node hello.js").stdout()
    if not match(expected, actual):
        help = None
        if match(expected[:-1], actual):
            help = r"did you forget a newline ('\n') at the end of your printf string?"
        raise check50.Mismatch("hello, world\n", actual, help=help)
