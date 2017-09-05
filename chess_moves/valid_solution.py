import chess_moves.move_finder as move_finder
import itertools

def is_valid_board(board):
    queens = [(i, b) for i in range(8) for b in range(8) if board[i][b] != "-"]
    #print queens
    #BUG: It is including itself when it finds all available moves!
    #return all(all("Q" not in board[c][b] for c, b in move_finder.get_queen_moves(board, i, j)) for i, j in queens)
    #return queens
    new_queens = {queen:[i for i in move_finder.get_queen_moves(board, queen[0], queen[-1]) if i != queen] for queen in queens}

    return all(all(board[c][d] == "-" for c, d in new_queens[q]) for q in new_queens)
    #return queens, new_queens, {q:[board[c][d] for c, d in new_queens[q]] for q in new_queens}
'''
f = [i.strip('\n') for i in open('/Users/jamespetullo/results.txt')]

f = [i for i in f if i != "-----------------"]

boards = [f[i:i+8] for i in range(0, len(f), 8)]
new_boards = [[b.split() for b in i] for i in boards]


count = 0
for board in new_boards:

    if is_valid_board(board):
        print "this is valid"
        for i in board:
            print ' '.join(i)
    else:
        print "this is not valid"
        for i in board:
            print ' '.join(i)



    for i in board:
        print ' '.join(i)
    queens, squares, values = is_valid_board(board)
    print squares
    print values

    if is_valid_board(board):
        for i in board:
            print ' '.join(i)
            #This works!



    print "----------------------"






    #print vals
'''
