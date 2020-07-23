import check50

@check50.check()
def exists():
    """plurality.py exists"""
    check50.exists("plurality.py")

@check50.check(exists)
def print_winner0():
    """print_winner identifies Alice as winner of election"""
    check50.run("python3 plurality.py Alice Bob").stdin("2").stdin("Alice").stdin("Alice").stdout("Alice\n").exit(0)

