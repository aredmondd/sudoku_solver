board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#this function just prints the board. it also adds lines for pretty formatting.
def print_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print ("- - - - - - - - - - - - - ")

        for col in range(len(board[0])):
            if col % 3 == 0 and col != 0:
                print (" | ", end="")

            if col == 8:
                print (board[row][col])
            else:
                print (str(board[row][col]) + " ", end="")

#find the first empty position
def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)

    return None #if board is full

#this is implementing the basic rules of sudoku. checking the row, the col, and the sqaure
def valid(board, number, position):
    #check the col
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    #check the row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False;

    #check the 3 x 3 square
    square_x = position[1] // 3
    square_y = position[0] // 3

    #loop through all elements in the 3 x 3 square
    for i in range(square_y * 3, square_x * 3 + 3):
        for j in range(square_x * 3, square_y * 3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False

    #if it's valid
    return True

#recursive function to solve using backtracking
def solve (board):
    #base case
    findOpenSpot = find_empty(board)
    if not findOpenSpot:
        return True
    else:
        row, col = findOpenSpot
    
    for i in range(1,10): #check if it's valid in the board
        if valid(board, i, (row,col)): #if valid, add
            board[row][col] = i
        
            if solve(board): #do the same thing on this new baord
                return True
            
            board[row][col] = 0; #backtrack, reset the tested one to 0.

    return False

print("Original Board: ")
print_board(board)
solve(board)
print("\n\nSolved Board:")
print_board(board)
