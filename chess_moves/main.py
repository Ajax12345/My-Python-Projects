import random
import copy
import pickle
import timeit
import chess_moves.move_finder as move_finder
import valid_solution

class Node:
    __slots__ = ['depth', 'board', 'queens', 'nodes', 'board_states', 'updated_states']
    def __init__(self, depth):
        self.depth = depth
        self.board = [['-', '-', '-', '-', '-', '-', '-', '-'],
                    ['-', '-', '-', '-', '-', '-', '-', '-'],
                    ['-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-'],
                      ['-', '-', '-', '-', '-', '-', '-', '-']]
        self.queens = {"Q{}".format(i+1):[] for i in range(8)}
        self.nodes = []
        self.board_states = []
        self.updated_states = []
    def the_tree(self):
        moves = [(i, b) for b in range(8) for i in range(8)]
        for coord1, coord2 in moves:
            self.new_board = copy.deepcopy(self.board)
            self.new_board[coord1][coord2] = "Q1"
            self.queens["Q1"] = [coord1, coord2]
            current_queens = ["Q1"]
            current_nodes = []
            current_nodes.append((coord1, coord2))
            for i in range(self.depth):
                home_base = None
                the_move = None
                nodes_seen = []
                nothing_found = False
                while True:
                    home_base = random.choice(current_nodes)
                    nodes_seen.append(home_base)
                    a, b = home_base
                    possible_moves = move_finder.get_knight_moves(copy.deepcopy(self.new_board), a, b)
                    best_possible_moves = [i for i in possible_moves if all("Q" not in self.new_board[a][b] for a, b in move_finder.get_queen_moves(self.new_board, i[0], i[1]))]
                    if best_possible_moves:
                        the_move = random.choice(best_possible_moves)
                        break
                    else:
                        if all(i in nodes_seen for i in current_nodes):
                            nothing_found = True
                            break
                        else:
                            continue
                if not nothing_found:
                    c, d = the_move
                    current_nodes.append((c, d))
                    self.new_board[c][d] = "Q{}".format(int(current_nodes[-1][-1])+1)
                    current_queens.append("Q{}".format(int(current_nodes[-1][-1])+1))
                else:
                    #reached node level
                    self.board_states.append(self.new_board)
                    break
        self.queens = {"Q{}".format(i+1):[] for i in range(8)}
        self.updated_states = list(self.tree_2(self.board_states))

    def tree_2(self, boards):
        for board in boards:
            current_queens = {}
            queen_data = sorted([board[i][b] for b in range(8) for i in range(8) if "Q" in board[i][b]], key=lambda x: int(x[-1]))

            last_queen = int(queen_data[-1][-1])

            queens_needed = 8-last_queen
            last_queen = queen_data[-1]
            possible_squares = [(i, b) for i in range(8) for b in range(8) if board[i][b] == "-"]
            final_boards = []
            for square in possible_squares:
                new_board1 = copy.deepcopy(board)
                a, b = square
                #last_queen = None
                nodes_used = []

                queen_name = "Q{}".format(int(last_queen[-1])+1)
                current_queens[queen_name] = square
                last_queen = queen_name
                nodes_used.append(square)
                #print "queens_needed", queens_needed
                nodes_seen = []
                for i in range(queens_needed):
                    to_terminate = False
                    while True:
                        home_base = random.choice(nodes_used)


                        possible_squares = move_finder.get_knight_moves(new_board1, home_base[0], home_base[-1])
                        new_possible_squares = [i for i in possible_squares if all("Q" not in new_board1[a][b] for a, b in move_finder.get_queen_moves(new_board1, i[0], i[1]))]
                        if new_possible_squares:
                            final_place = random.choice(new_possible_squares)
                            c, d = final_place
                            nodes_used.append(final_place)
                            queen_name = "Q{}".format(int(last_queen[-1])+1)
                            last_queen = queen_name
                            current_queens[queen_name] = final_place
                            new_board1[c][d] = queen_name



                        else:
                            to_terminate = True
                            break
                    if to_terminate:
                        break
                if sum(1 for i in range(8) for b in range(8) if "Q" in new_board1[b][i]) == 7:
                    if [(i, b) for i in range(8) for b in range(8) if new_board1[b][i] == "-" and all(new_board1[c][d] == "-" for c, d in move_finder.get_queen_moves(new_board1, i, b))]:
                        try:
                            [new_stuff] = [(i, b) for i in range(8) for b in range(8) if new_board1[b][i] == "-" and all(new_board1[c][d] == "-" for c, d in move_finder.get_queen_moves(new_board1, i, b))]
                            a, b = new_stuff
                            new_board1[a][b] = "Qf"
                            yield new_board1

                        except ValueError:
                            pass






    def show_boards(self):

        pickle.dump(self.updated_states, open('queens_puzzle_results.txt', 'a'))

        return self.updated_states


class Queens:
    def __init__(self):
        self.board = [['-', '-', '-', '-', '-', '-', '-', '-'],
                    ['-', '-', '-', '-', '-', '-', '-', '-'],
                    ['-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-'],
                      ['-', '-', '-', '-', '-', '-', '-', '-']]

        self.queens = {"Q{}".format(i+1):[] for i in range(8)}
        self.clusters = 1


    def tree(self):
        pass

        moves = [(i, b) for b in range(8) for i in range(8)]
        for coord1, coord2 in moves:
            pass
final_boards = []
start_time = timeit.default_timer()
print "starting here"
for i in range(50):
    branch = Node(8)
    branch.the_tree()

    for board in branch.show_boards():
        if board not in final_boards:
            if valid_solution.is_valid_board(board):
                final_boards.append(board)

for board in final_boards:
    for row in board:
        for square in row:
            print square,

        print
    print "-----------------"

elapsed = timeit.default_timer() - start_time

print "number of solutions found:", len(final_boards)
print "time:", elapsed, " seconds"
