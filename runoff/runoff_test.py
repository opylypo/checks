import sys

from plurality import vote, tabulate, print_winner, find_min, is_tie, eliminate, Candidate
from dataclasses import dataclass

@dataclass
class Preference():
    def __init__(self, voter, rank, candidate):
        self.voter = voter
        self.rank = rank
        self.candidate = candidate

def main():    
    global candidates
    global preferences
    global candidate_count
    global voter_count
    
    candidates = []
    preferences = []

    # Determine which test to run
    setup = int(sys.argv[1])
    test = int(sys.argv[2])   
                   
    if setup == 0:
        voter_count = 5
        candidate_count = 3
        candidates.append(Candidate('Alice', 0, False))
        candidates.append(Candidate('Bob', 0, False))
        candidates.append(Candidate('Charlie', 0, False))
        
    elif setup == 1:
        voter_count = 7
        candidate_count = 4
        candidates.append(Candidate('Alice', 0, False))
        candidates.append(Candidate('Bob', 0, False))
        candidates.append(Candidate('Charlie', 0, False))
        candidates.append(Candidate('David', 0, False))
        preferences.append(Preference(0, 0, 0))
        preferences.append(Preference(1, 0, 0))
        preferences.append(Preference(0, 1, 1))
        preferences.append(Preference(1, 1, 1))
        preferences.append(Preference(0, 2, 2))
        preferences.append(Preference(1, 2, 2))
        preferences.append(Preference(0, 3, 3))
        preferences.append(Preference(1, 3, 3))               
        preferences.append(Preference(2, 0, 1))
        preferences.append(Preference(3, 0, 1))
        preferences.append(Preference(4, 0, 1))
        preferences.append(Preference(2, 1, 3))
        preferences.append(Preference(3, 1, 3))
        preferences.append(Preference(4, 1, 3))
        preferences.append(Preference(2, 2, 0))
        preferences.append(Preference(3, 2, 0))
        preferences.append(Preference(4, 2, 0))
        preferences.append(Preference(2, 2, 2))
        preferences.append(Preference(3, 2, 2))
        preferences.append(Preference(4, 2, 2))
        preferences.append(Preference(5, 0, 2))
        preferences.append(Preference(5, 1, 1))
        preferences.append(Preference(5, 2, 3))
        preferences.append(Preference(5, 3, 0))
        preferences.append(Preference(6, 0, 0))
        preferences.append(Preference(6, 1, 2))
        preferences.append(Preference(6, 2, 1))
        preferences.append(Preference(6, 3, 3))
        
    elif setup == 2:
        voter_count = 28
        candidate_count = 4
        candidates.append(Candidate('Alice', 8, False))
        candidates.append(Candidate('Bob', 15, False))
        candidates.append(Candidate('Charlie', 4, False))
        candidates.append(Candidate('David', 1, False))
            
    if test == 0:
        print(vote(0, 0, "Bob"))
        
    elif test == 1:
        print(vote(1, 2, "David"))
            
    elif test == 2:
        vote(0, 0, "Charlie")
        print(len(preferences) == 1 and preferences[0] == Preference(0, 0, 2))
        
    elif test == 3:
        vote(1, 2, "Alice")
        print(len(preferences) == 1 and preferences[0] == Preference(1, 2, 0))
        
    elif test == 4:
        vote(1, 0, "Bob")
        vote(1, 1, "Alice")
        vote(1, 2, "Charlie")
        print(len(preferences) == 3 and preferences[0] == Preference(1, 0, 2) and preferences[1] == Preference(1, 1, 0) and preferences[2] == Preference(1, 2, 2))
        
    elif test == 5:
        tabulate()
        for candidate in candidates:
            print(candidate.votes)
            
    elif test == 6:     
        candidates[3].eliminated = True
        tabulate()
        for candidate in candidates:
            print(candidate.votes)
            
    elif test == 7:
        candidates[2].eliminated = True
        candidates[3].eliminated = True
        tabulate()
        for candidate in candidates:
            print(candidate.votes)
            
    elif test == 8:
        print_winner()
        
    elif test == 9:
        print(print_winner())
        
    elif test == 10:
        candidates[0].votes = 11
        candidates[1].votes = 12;
        print(print_winner())
        
    elif test == 11:
        candidates[0].votes = 9
        candidates[1].votes = 14
        print(print_winner())
        
    elif test == 12:
        print(find_min())
        
    elif test == 13:
        candidates[0].votes = 7
        candidates[1].votes = 7
        candidates[2].votes = 7
        candidates[3].votes = 7
        print(find_min())
        
    elif test == 14:    
        candidates[3].eliminated = True
        candidates[2].votes = 5
        print(find_min())
        
    elif test == 15:
        candidates[0].votes = 7
        candidates[1].votes = 7
        candidates[2].votes = 7
        candidates[3].votes = 7
        print(is_tie(7))
        
    elif test == 16:
        candidates[0].votes = 5
        candidates[1].votes = 6
        candidates[2].votes = 8
        candidates[3].votes = 9
        print(is_tie(5))
        
    elif test == 17:
        candidates[0].votes = 6
        candidates[1].votes = 6
        candidates[2].votes = 8
        candidates[3].votes = 8
        print(is_tie(6))
        
    elif test == 18:
        candidates[0].votes = 7
        candidates[1].votes = 7
        candidates[2].votes = 0
        candidates[3].votes = 0
        candidates[2].eliminated = True
        candidates[3].eliminated = True
        print(is_tie(7))
        
    elif test == 19:
        eliminate(1)
        for candidate in candidates:
            print(candidate.eliminated)
            
    elif test == 20:
        candidates[0].votes = 6
        candidates[1].votes = 8
        candidates[2].votes = 6
        candidates[3].votes = 8
        eliminate(6)
        for candidate in candidates:
            print(candidate.eliminated)
            
    elif test == 21:
        candidates[0].votes = 0
        candidates[0].eliminated = True
        candidates[1].votes = 8
        candidates[2].votes = 6
        candidates[3].votes = 7
        eliminate(6)
        for candidate in candidates:
            print(candidate.eliminated)

if __name__ == "__main__":
    main()
