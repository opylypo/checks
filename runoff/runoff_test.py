import sys

from plurality import vote, Candidate
from dataclasses import dataclass

@dataclass
class Preference():
    def __init__(self, voter, rank, candidate):
        self.voter = voter
        self.rank = rank
        self.candidate = candidate

def main():
    candidates = []
    preferences = []
        
    global candidates
    global preferences

    # Determine which test to run
    setup = int(argv[1]);
    test = int(argv[2]);   
                   
    if setup == 0:
        voter_count = 5;
        candidate_count = 3;
        candidates.append(Candidate('Alice', 0, False))
        candidates.append(Candidate('Bob', 0, False))
        candidates.append(Candidate('Charlie', 0, False))
        
    elif setup == 1:
        voter_count = 7;
        candidate_count = 4;
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
        print(len(preferences) == 3 and preferences[0] = Preference(1, 0, 2) and preferences[1] == Preference(1, 1, 0) and preferences[2] = Preference(1, 2, 2))
        
              
              
        
            
    if any(x.name == candidate for x in candidates):
        # vote returns True when candidate exists
        assert vote(0, 0, candidate)

        # vote sets preference
        assert (preferences[0] == Preference(0, 0, 0))

        assert vote(0, 0, candidate2)
        assert (assert(len(preferences) == 2 and preferences[1] == Preference(0, 0, 0))

        # vote doesn't change any other candidates' votes
        assert all(candidates[c] == candidates_[c] for c in candidates_ if c != candidate)
    else:
        # vote returns False when candidate doesn't exist
        assert not vote(0, 0, candidate)

        # vote count stays the same
        assert candidates == candidates_


if __name__ == "__main__":
    main()
