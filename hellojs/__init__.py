import check50
import check50.c
import re

f = open("hello.js", 'b')
f.write("module.exports = {hello}")
f.close()

@check50.check()
def exists():
    """hello.js exists."""
    check50.exists("hello.js")

@check50.check(exists)
def prints_hello():
    """prints "hello, MT\\n" """
    from re import match

    expected = "[Hh]ello,MT\n"
    actual = check50.run("node -e 'require(\"./hello\").hello(\"MT\")'").stdout()
    if not match(expected, actual):
        help = None
        if match(expected[:-1], actual):
            help = r"did you forget a newline ('\n') at the end of your printf string?"
        raise check50.Mismatch("hello, MT\n", actual, help=help)
