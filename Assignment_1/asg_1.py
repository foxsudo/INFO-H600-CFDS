

                  ###################################################################
                  # Assignment 1 : INFO-H600 Computing Foundations of Data Sciences #
                  ###################################################################

######################################################
# Exercices 1 : The Sequence (Look-and-say sequence) #
######################################################

def the_sequence(n):
    # Base case: if n is 0 or negative, return an empty list
    if n <= 0:
        return []
    
    # If n == 1, return the first term of the sequence
    if n == 1:
        return ['1']
    
    # Recursive call: generate the sequence up to (n - 1)
    seq = the_sequence(n - 1)
    
    # Get the last (most recent) term in the sequence
    prev = seq[-1]
    
    # Initialize variables for building the next term
    next_term = ""  # will store the next string in the sequence
    count = 1       # counts consecutive identical digits
    
    # Loop through the previous term starting from the 2nd character
    for i in range(1, len(prev)):
        if prev[i] == prev[i-1]:
            # If the current digit is the same as the previous one, increase the count
            count += 1
        else:
            # If the digit changes:
            # append "count + previous_digit" to next_term
            next_term += str(count) + prev[i-1]
            # reset the counter for the new digit
            count = 1
    
    # After the loop ends, append the last counted group
    next_term += str(count) + prev[-1]
    
    # Add the newly formed term to the sequence
    seq.append(next_term)
    
    # Return the complete sequence up to n terms
    return seq

# Calling the function for exercise 1

print(the_sequence(8))

################################################
# Exercices 2 : Validity of 9 × 9 Sudoku board #
################################################

def is_valid_sudoku(board):
    # Create 9 sets for rows, columns, and 3x3 boxes
    # Each set will store the digits already seen in that row/column/box
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    # Loop through every cell in the 9x9 Sudoku grid
    for i in range(9):          # iterate over rows
        for j in range(9):      # iterate over columns
            val = board[i][j]   # current cell value
            
            # Skip empty cells (represented by '.')
            if val != '.':
                # Compute which 3x3 sub-box this cell belongs to
                # Boxes are indexed from 0 to 8:
                box_idx = (i // 3) * 3 + (j // 3)
                
                # If the number is already in the same row, column, or box then the board is invalid Sudoku
                if val in rows[i] or val in cols[j] or val in boxes[box_idx]:
                    return False
                
                # Otherwise, add the number to the respective sets
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_idx].add(val)
    
    # If no conflicts were found, the Sudoku board is valid
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

##############################################
# Exercices 3 : Tic-Tac-Toe Validity Checker #
##############################################

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

