

                  ###################################################################
                  # Assignment 1 : INFO-H600 Computing Foundations of Data Sciences #
                  ###################################################################

######################################################
# Exercices 1 : The Sequence (Look-and-say sequence) #
######################################################

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

################################################
# Exercices 2 : Validity of 9 × 9 Sudoku board #
################################################

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

##################################
# Exercices 3 : Tic-Tac-Toe game #
##################################

def is_valid_tictactoe(board):
    # Count the X's and O's
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    
    # Rule 1: X starts → X = O or X = O + 1
    if not (x_count == o_count or x_count == o_count + 1):
        return False

    # Function to check if a player has won
    def win(player):
        # Lines
        for row in board:
            if all(cell == player for cell in row):
                return True
        # Colomns
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        # Diagonals
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2-i] == player for i in range(3)):
            return True
        return False
    
    x_win = win('X')
    o_win = win('O')
    
    # Rules 2 and 3: Both cannot win together
    if x_win and o_win:
        return False
    if x_win and x_count != o_count + 1:
        return False
    if o_win and x_count != o_count:
        return False
    
    return True

# Calling the function for exercise 3
print(is_valid_tictactoe(['XXX', ' X ', '   ']))  # ==> False
print(is_valid_tictactoe(['XOX', ' O ', '   ']))  # ==> True
print(is_valid_tictactoe(['O  ', '   ', '   ']))  # ==> False
print(is_valid_tictactoe(['X  ', '   ', '   ']))  # ==> True
print(is_valid_tictactoe(['XOX', ' X ', '   ']))  # ==> False
