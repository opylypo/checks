from plurality_test import vote, print_winner
from sys import argv

# Check for invalid usage
if len(argv) != 2:
    exit(0)

test = int(argv[1])

candidate_count = 3
# candidates = {}

# candidates["Alice"] = 0
# candidates["Bob"] = 0
# candidates["Charlie"] = 0

def case0():
    print(vote("Alice"))

def case1():
    print(vote("David"))

# map the inputs to the function blocks
options = {0 : case0,
           1 : case1
}

options[test]()





