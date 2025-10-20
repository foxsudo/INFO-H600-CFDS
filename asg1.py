###############
# Exercices 1 #
###############

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
print(the_sequence(8))

###############
# Exercices 2 #
###############

# Validity of 9 × 9 Sudoku board

def is_valid_sudoku(board):
    # Checking the lines
    for row in board:
        nums = [c for c in row if c != '.']
        if len(nums) != len(set(nums)):
            return False

    # Checking the columns
    for col in range(9):
        nums = [board[row][col] for row in range(9) if board[row][col] != '.']
        if len(nums) != len(set(nums)):
            return False

    # Checking 3x3 subgrids
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            nums = []
            for i in range(3):
                for j in range(3):
                    val = board[box_row + i][box_col + j]
                    if val != '.':
                        nums.append(val)
            if len(nums) != len(set(nums)):
                return False

    return True

# Exemple of Board
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

# Calling the function for exercise 2
print(is_valid_sudoku(board))  # ==> True


