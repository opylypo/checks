import check50

@check50.check()
def exists():
    """plurality.py exists"""
    check50.exists("plurality.py")
    
@check50.check(exists)
def prepare():
    """test file created"""
    plurality = open("plurality.py")
    plurality_test = open("plurality_test.py", "w")

    plurality_test.write(plurality.read())
    plurality_test.write("\n\ncandidates['Alice'] = 0\ncandidates['Bob'] = 0\ncandidates['Charlie'] = 0")

    plurality.close()
    plurality_test.close()
    

@check50.check(compiles)
@check50.hidden("vote function did not return True")
def vote_finds_name():
    """vote returns true when given name of candidate"""
    check50.run("python3 testing.py 0").stdout("True").exit(0)
  

@check50.check(compiles)
@check50.hidden("vote function did not return False")
def vote_returns_false():
    """vote returns false when given name of invalid candidate"""
    check50.run("python3 testing.py 1").stdout("False").exit(0)
  

@check50.check(exists)
def print_winner0():
    """print_winner identifies Alice as winner of election"""
    check50.run("python3 plurality.py Alice Bob").stdin("2").stdin("Alice").stdin("Alice").stdout("Alice\n").exit(0)

