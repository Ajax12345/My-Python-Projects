import copy
import random
from itertools import chain
#this is entirly written in python 3
class MiniGame:
    def __init__(self, board):
        self.board = board
        #self.square = square

    def possible_squares_o(self):
        yield from [(i, b) for i in range(3) for b in range(3) if self.board[i][b] == "-"]
    def possible_squares_x(self):
        yield from [(i, b) for i in range(3) for b in range(3) if self.board[i][b] == "-"]

    def make_move(self):
        o_moves = list(self.possible_squares_o())
        a, b = random.choice(o_moves)
        self.board[a][b] = "o"

        x_moves = list(self.possible_squares_x())

        a1, b1 = random.choice(x_moves)
        self.board[a1][b1] = "x"

class TackToe:
    def __init__(self):
        self.board = [["-" for i in range(3)] for b in range(3)]
        self.results = {}
        self.the_winner = None

    def print_board(self):
        for i, a in enumerate(self.board):
            if i == len(self.board) -1:
                print(' | '.join(a))

            else:
                print(' | '.join(a))
                print("----------")

    def get_possible_squares(self):
        yield from [(i, b) for i in range(3) for b in range(3) if self.board[i][b] == "-"]

    def play(self):
        moves = list(self.get_possible_squares())
        possibilities = {}
        for move in moves:
            #print("move", move)
            self.determine_outcome(move)

    def winner(self, the_board):
        #determine who one
        top = all(i == "o" for i in the_board[0])
        middle = all(i == "o" for i in the_board[1])
        bottom = all(i == "o" for i in the_board[-1])
        side = all(i == "o" for i in list(zip(*the_board))[0])
        side1 = all(i == "o" for i in list(zip(*the_board))[1])
        side2 = all(i == "o" for i in list(zip(*the_board))[-1])
        diagonal1 = all(the_board[i][i] == "o" for i in range(3))
        diagonal2 = all(the_board[2-i][i] == "o" for i in range(3))

        top1 = all(i == "x" for i in the_board[0])
        middle1 = all(i == "x" for i in the_board[1])
        bottom1 = all(i == "x" for i in the_board[-1])
        side01 = all(i == "x" for i in list(zip(*the_board))[0])
        side11 = all(i == "x" for i in list(zip(*the_board))[1])
        side21 = all(i == "x" for i in list(zip(*the_board))[-1])
        diagonal11 = all(the_board[i][i] == "x" for i in range(3))
        diagonal21 = all(the_board[2-i][i] == "x" for i in range(3))

        #print("-------------------")
        if any([top, middle, bottom, side, side1, side2, diagonal1, diagonal2]) or any([top1, middle1, bottom1, side01, side11, side21, diagonal11, diagonal21]):
            return True

        elif not any([top, middle, bottom, side, side1, side2, diagonal1, diagonal2]) and not any([top1, middle1, bottom1, side01, side11, side21, diagonal11, diagonal21]) and "-" not in chain.from_iterable(the_board):
            return True

    def determine_final_winner(self):
        top = all(i == "o" for i in self.board[0])
        middle = all(i == "o" for i in self.board[1])
        bottom = all(i == "o" for i in self.board[-1])
        side = all(i == "o" for i in list(zip(*self.board))[0])
        side1 = all(i == "o" for i in list(zip(*self.board))[1])
        side2 = all(i == "o" for i in list(zip(*self.board))[-1])
        diagonal1 = all(self.board[i][i] == "o" for i in range(3))
        diagonal2 = all(self.board[2-i][i] == "o" for i in range(3))

        top1 = all(i == "x" for i in self.board[0])
        middle1 = all(i == "x" for i in self.board[1])
        bottom1 = all(i == "x" for i in self.board[-1])
        side01 = all(i == "x" for i in list(zip(*self.board))[0])
        side11 = all(i == "x" for i in list(zip(*self.board))[1])
        side21 = all(i == "x" for i in list(zip(*self.board))[-1])
        diagonal11 = all(self.board[i][i] == "x" for i in range(3))
        diagonal21 = all(self.board[2-i][i] == "x" for i in range(3))

        #print("-------------------")
        if any([top, middle, bottom, side, side1, side2, diagonal1, diagonal2]) or any([top1, middle1, bottom1, side01, side11, side21, diagonal11, diagonal21]):
            return True

        elif not any([top, middle, bottom, side, side1, side2, diagonal1, diagonal2]) and not any([top1, middle1, bottom1, side01, side11, side21, diagonal11, diagonal21]) and "-" not in chain.from_iterable(self.board):
            return True



    def who_one(self, the_board):
        top = all(i == "o" for i in the_board[0])
        middle = all(i == "o" for i in the_board[1])
        bottom = all(i == "o" for i in the_board[-1])
        side = all(i == "o" for i in list(zip(*the_board))[0])
        side1 = all(i == "o" for i in list(zip(*the_board))[1])
        side2 = all(i == "o" for i in list(zip(*the_board))[-1])
        diagonal1 = all(the_board[i][i] == "o" for i in range(3))
        diagonal2 = all(the_board[2-i][i] == "o" for i in range(3))

        top1 = all(i == "x" for i in the_board[0])
        middle1 = all(i == "x" for i in the_board[1])
        bottom1 = all(i == "x" for i in the_board[-1])
        side01 = all(i == "x" for i in list(zip(*the_board))[0])
        side11 = all(i == "x" for i in list(zip(*the_board))[1])
        side21 = all(i == "x" for i in list(zip(*the_board))[-1])
        diagonal11 = all(the_board[i][i] == "x" for i in range(3))
        diagonal21 = all(the_board[2-i][i] == "x" for i in range(3))

        if any([top, middle, bottom, side, side1, side2, diagonal1, diagonal2]):
            #return "o"
            return "o"

        else:
            if any([top1, middle1, bottom1, side01, side11, side21, diagonal11, diagonal21]):
                return "x"

            else:
                return "tie"






    def determine_outcome(self, square):
        new_game = MiniGame(copy.deepcopy(self.board))
        a, b = square
        new_game.board[a][b] = "o"
        while not self.winner(new_game.board):
            #for row in new_game.board:
                #print(row)
            #print("--------------------")
            new_game.make_move()


            #self.who_one(new_game.board)


        result = self.who_one(new_game.board)

        if result == "o":
            self.results[square] = 1
        else:
            if result == "tie":
                self.results[square] = 0.5
            else:
                self.results[square] = 0



    def decide_move(self):
        first_choice = [a for a, b in self.results.items() if b == 1]
        second_choice = [a for a, b in self.results.items() if b == 0.5]
        #print(self.results)
        the_square = None
        print(self.results)
        if first_choice:
            the_square = random.choice(first_choice)

        else:
            if second_choice:
                the_square = random.choice(second_choice)

            else:
                the_square = random.choice(list(self.results.keys()))

        a, b = the_square
        self.board[a][b] = "o"
        self.results = {}

    def user_move(self):
        x = int(input("enter the x-corrindate: "))
        y = int(input("enter the y-corrdnate: "))
        self.board[x-1][y-1] = "x"

    def __str__(self):
        return "result: {}".format(self.the_winner)







if __name__ == "__main__":
    t = TackToe()
    #t.print_board()
    #while not t.determine_final_winner():

    while not t.determine_final_winner():
        t.play()
        t.decide_move()
        #t.print_board()
        print("----------------")
        t.user_move()
        t.print_board()
