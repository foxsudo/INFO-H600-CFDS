# Exercices 1

#Create a function the_sequence that accepts one integer and returns a list of strings representing 
#the following sequence: 1, 11, 21, 1211, 111221, 312211, 13112221, . . . .

def the_sequence(n):
    # Check for n <= 0
    if n <= 0:
        return []
    
    # Initialization of the sequence with the first term
    seq = ['1']
    
    # Generation of the following terms
    for _ in range(1, n):
        prev = seq[-1]  # last term
        next_term = ""
        count = 1
        
        # Parcours du terme actuel pour le "lire"
        for i in range(1, len(prev)):
            if prev[i] == prev[i-1]:
                count += 1
            else:
                next_term += str(count) + prev[i-1]
                count = 1
        # Add last group
        next_term += str(count) + prev[-1]
        
        seq.append(next_term)
    
    return seq

# Calling the function for exercise 1
# print(the_sequence(8))

