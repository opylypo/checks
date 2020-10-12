import check50
import re

@check50.check()
def exists():
    """runoff.py exists"""
    check50.exists("runoff.py")
    check50.include("runoff_test_functions.py")
    runoff = re.sub("main", "distro_main", open("runoff.py").read())
    testing = open("runoff_test_functions.py").read()
    with open("runoff_test.py", "w") as f:
        f.write(runoff)
        f.write("\n")
        f.write(testing)


@check50.check(exists)
@check50.hidden("vote function did not return true")
def vote_returns_true():
     """vote returns true when given name of candidate"""
     check50.run("python3 runoff_test.py 0 0").stdout("True").exit(0)


@check50.check(exists)
@check50.hidden("vote function did not return false")
def vote_returns_false():
    """vote returns false when given name of invalid candidate"""
    check50.run("python3 runoff_test.py 0 1").stdout("False").exit(0)


@check50.check(exists)
@check50.hidden("vote function did not correctly set preferences")
def vote_sets_preference1():
    """vote correctly sets first preference for first voter"""
    check50.run("python3 runoff_test.py 0 2").stdout("2").exit(0)


@check50.check(exists)
def vote_sets_preference2():
    """vote correctly sets third preference for second voter"""
    check50.run("python3 runoff_test.py 0 3").stdout("0").exit(0)


@check50.check(exists)
@check50.hidden("vote function did not correctly set preferences")
def vote_sets_all_preferences():
    """vote correctly sets all preferences for voter"""
    check50.run("python3 runoff_test.py 0 4").stdout("1 0 2").exit(0)
    

@check50.check(exists)
@check50.hidden("tabulate function did not produce correct vote totals")
def tabulate1():
    """tabulate counts votes when all candidates remain in election"""
    check50.run("python3 runoff_test.py 1 5").stdout("3\n3\n1\n0\n").exit(0)
        

@check50.check(exists)
@check50.hidden("tabulate function did not produce correct vote totals")
def tabulate2():
    """tabulate counts votes when one candidate is eliminated"""
    check50.run("python3 runoff_test.py 1 6").stdout("3\n3\n1\n0\n").exit(0)
        

@check50.check(exists)
@check50.hidden("tabulate function did not produce correct vote totals")
def tabulate3():
    """tabulate counts votes when multiple candidates are eliminated"""
    check50.run("python3 runoff_test.py 1 7").stdin("5").stdout("3\n4\n0\n0\n").exit(0)
    
    
@check50.check(exists)
@check50.hidden("print_winner did not print winner of election")
def print_winner1():
    """print_winner prints name when someone has a majority"""
    check50.run("python3 runoff_test.py 2 8").stdout("Bob\n").exit(0)
    
@check50.check(exists)
@check50.hidden("print_winner did not print winner and then return true")
def print_winner2():
    """print_winner returns true when someone has a majority"""
    check50.run("python3 runoff_test.py 2 9").stdout("Bob\nTrue").exit(0)

@check50.check(exists)
@check50.hidden("print_winner did not return false")
def print_winner3():
    """print_winner returns false when nobody has a majority"""
    check50.run("python3 runoff_test.py 2 10").stdout("False").exit(0)

@check50.check(exists)
@check50.hidden("print_winner did not return false")
def print_winner4():
    """print_winner returns false when leader has exactly 50% of vote"""
    check50.run("python3 runoff_test.py 2 11").stdout("False").exit(0)

@check50.check(exists)
@check50.hidden("find_min did not identify correct minimum")
def find_min1():
    """find_min returns minimum number of votes for candidate"""
    check50.run("python3 runoff_test.py 2 12").stdout("1").exit(0)

@check50.check(exists)
@check50.hidden("find_min did not identify correct minimum")
def find_min2():
    """find_min returns minimum when all candidates are tied"""
    check50.run("python3 runoff_test.py 2 13").stdout("7").exit(0)

@check50.check(exists)
@check50.hidden("find_min did not identify correct minimum")
def find_min3():
    """find_min ignores eliminated candidates"""
    check50.run("python3 runoff_test.py 2 14").stdout("5").exit(0)

@check50.check(exists)
@check50.hidden("is_tie did not return true")
def is_tie1():
    """is_tie returns true when election is tied"""
    check50.run("python3 runoff_test.py 2 15").stdout("True").exit(0)

@check50.check(exists)
@check50.hidden("is_tie did not return false")
def is_tie2():
    """is_tie returns false when election is not tied"""
    check50.run("python3 runoff_test.py 2 16").stdout("False").exit(0)

@check50.check(exists)
@check50.hidden("is_tie did not return false")
def is_tie3():
    """is_tie returns false when only some of the candidates are tied"""
    check50.run("python3 runoff_test.py 2 17").stdout("False").exit(0)

@check50.check(exists)
@check50.hidden("is_tie did not return true")
def is_tie4():
    """is_tie detects tie after some candidates have been eliminated"""
    check50.run("python3 runoff_test.py 2 18").stdout("True").exit(0)

@check50.check(exists)
@check50.hidden("eliminate did not eliminate correct candidates")
def eliminate1():
    """eliminate eliminates candidate in last place"""
    check50.run("python3 runoff_test.py 2 19").stdout("False False False True ").exit(0)

@check50.check(exists)
@check50.hidden("eliminate did not eliminate correct candidates")
def eliminate2():
    """eliminate eliminates multiple candidates in tie for last"""
    check50.run("python3 runoff_test.py 2 20").stdout("True False True False ").exit(0)

@check50.check(exists)
@check50.hidden("eliminate did not eliminate correct candidates")
def eliminate3():
    """eliminate eliminates candidates after some already eliminated"""
    check50.run("python3 runoff_test.py 2 21").stdout("True False True False ").exit(0)    
    
    
    
    
