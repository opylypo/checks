import check50
import check50.c
import re


@check50.check()
def exists(self):
    """syntax.c exists."""
    check50.exists("syntax.c")


@check50.check(exists)
def compiles():
    """syntax.c compiles."""
    check50.c.compile("syntax.c", lcs50=True)


@check50.check(compiles)
def prints_thisiscs50ap():
    """prints "This is CS50AP!\\n" """
    expected = "[Tt]his is CS50AP!?\n"
    actual = check50.run("./syntax").stdout()
    if not re.match(expected, actual):
        err = Error(Mismatch("This is CS50AP!\n", actual))
        if re.match(expected[:-1], actual):
            err.helpers = "Did you forget a newline (\"\\n\") at the end of your printf string?"
        raise err
