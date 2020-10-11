from sys import argv

# Check for invalid usage
if len(argv) != 2:
    exit(0)

test = int(argv[1])

# Setup
candidate_count = 3
candidates["Alice"] = 0
candidates["Bob"] = 0
candidates["Charlie"] = 0

# Tests
def case0():
    print(vote("Alice"))


def case1():
    print(vote("Bob"))


def case2():
    print(vote("Charlie"))


def case3():
    print(vote("David"))


def case4():
    vote("Alice")
    print(candidates["Alice"], candidates["Bob"], candidates["Charlie"])

def case5():
    candidates["Alice"] = 2
    candidates["Bob"] = 7
    candidates["Charlie"] = 0
    vote("Bob")
    print(candidates["Alice"], candidates["Bob"], candidates["Charlie"])

def case6():
    candidates["Alice"] = 2
    candidates["Bob"] = 8
    candidates["Charlie"] = 0
    vote("David")
    print(candidates["Alice"], candidates["Bob"], candidates["Charlie"])


def case7():
    candidates["Alice"] = 8
    candidates["Bob"] = 2
    candidates["Charlie"] = 0
    print_winner()


def case8():
    candidates["Alice"] = 1
    candidates["Bob"] = 8
    candidates["Charlie"] = 2
    print_winner()


def case9():
    candidates["Alice"] = 1
    candidates["Bob"] = 8
    candidates["Charlie"] = 9
    print_winner()


def case10():
    candidates["Alice"] = 8
    candidates["Bob"] = 8
    candidates["Charlie"] = 5
    print_winner()


def case11():
    candidates["Alice"] = 8
    candidates["Bob"] = 8
    candidates["Charlie"] = 8
    print_winner()


# map the inputs to the function blocks
options = {0 : case0,
           1 : case1,
           2 : case2,
           3 : case3,
           4 : case4,
           5 : case5,
           6 : case6,
           7 : case7,
           8 : case8,
           9 : case9,
           10: case10,
           11: case11

}

options[test]()
