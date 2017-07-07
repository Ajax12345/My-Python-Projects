#1 Carrier: 5 stars
#2 Battleship: 4 stars
#3 Cruiser: 3 stars
#4 Submarine: 3 stars
#5 Destoyer: 2 stars
#star denotes part of ship
#TODO: display coordinates of last successful enemy hit
import string
import random


class Battleship:
    def __init__(self):
        self.opponent_server_side = [['-', '*', '*', '*', '-', '-', '-', '-'], #stores the ships of the opponent
                                    ['-', '-', '-', '-', '-', '-', '-', '-'],
                                    ['*', '-', '-', '-', '-', '-', '-', '-'],
                                    ['*', '-', '*', '*', '*', '*', '*', '-'],
                                    ['-', '-', '-', '-', '-', '-', '-', '-'],
                                    ['-', '-', '*', '*', '*', '*', '-', '-'],
                                    ['_', '-', '-', '-', '-', '-', '-', '-'],
                                    ['-', '-', '-', '-', '-', '*', '*', '*']]

        self.opponent_client_side = [['-', '-', '-', '-', '-', '-', '-', '-'], #stores what the user sees of the the opponent
                                    ['-', '-', '-', '-', '-', '-', '-', '-'],
                                    ['-', '-', '-', '-', '-', '-', '-', '-'],
                                    ['-', '-', '-', '-', '-', '-', '-', '-'],
                                    ['-', '-', '-', '-', '-', '-', '-', '-'],
                                    ['-', '-', '-', '-', '-', '-', '-', '-'],
                                    ['-', '-', '-', '-', '-', '-', '-', '-'],
                                    ['-', '-', '-', '-', '-', '-', '-', '-']]

        self.user_server_side = [['-', '-', '-', '-', '-', '-', '-', '-'], #stores the ships of the user
                                ['-', '*', '*', '*', '*', '*', '-', '-'],
                                ['-', '-', '-', '-', '-', '-', '-', '-'],
                                ['-', '-', '-', '-', '-', '-', '-', '-'],
                                ['*', '-', '*', '-', '*', '*', '-', '-'],
                                ['*', '-', '*', '-', '-', '-', '-', '-'],
                                ['*', '-', '*', '-', '-', '-', '-', '-'],
                                ['*', '-', '-', '-', '-', '*', '*', '*']]

        self.user_client = [['-', '-', '-', '-', '-', '-', '-', '-'], #what the opponent uses to guess ship location
                            ['-', '-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-', '-']]

        self.user_ship_location = {"Carrier":[(1, i) for i in range(1, 6)],
                                    "Battleship":[(i, 0) for i in range(4, 8)],
                                    "Cruiser":[(i, 2) for i in range(4, 7)],
                                    "Submarine":[(7, i) for i in range(5, 8)],
                                    "Destroyer":[(4, i) for i in range(4, 6)]}  #this dict stores the locations for all the ships of the human player

        self.enemy_ship_location = {"Carrier":[(3, i) for i in range(2, 7)],
                                    "Battleship":[(5, i) for i in range(2, 6)],
                                    "Cruiser":[(7, i) for i in range(5, 8)],
                                    "Submarine":[(0, i) for i in range(1, 4)]}

        self.converter = {'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 'H': 8, 'K': 11, 'J': 10}

        self.last_hit = []

        self.opening_count = 0

        self.sunk = False

        self.hit = False

        self.enemy_ships_sunk = []

        self.user_ships_sunk = []

        self.hit_last = False

        self.try_top = False  #this flag alerts us that we reached the end of part of the ship, and need to try from the other side
        self.try_bottom = False

        self.last_user_moves = []

    def can_play(self):
        return not len(self.enemy_ships_sunk) == 5 or len(self.user_ships_sunk) == 5

    def enemy_sunk(self):
        for a, b in self.enemy_ship_location.items():
            if all(i in b for i in self.last_user_moves) and len(self.last_user_moves) == len(b):
                print "YOU SUNK AN ENEMY", a.upper()
                for c in self.last_user_moves:
                    self.opponent_server_side[c[0]][c[1]] = "-"
                self.last_user_moves = []

                break



    def determine_winner(self):
        if len(self.user_ships_sunk) == 5:
            print "YOU LOST!"

        elif len(self.enemy_ships_sunk) == 5:
            print "YOU WON!"

    def determine_sunk_user(self):
        if self.sunk:
            for a, b in self.user_ship_location:
                if all(i in b for i in self.last_hit) and len(self.last_hit):
                    print a.upper(), "Sunk"
                    self.user_ships_sunk.append(a)

                    for c in b:
                        self.user_server_side[c[0]][c[1]] = "-"
                    break

            self.last_hit = []
            self.hit_last = False
            self.try_top = False
            self.try_bottom = False



    def opponent_move(self):
        if not self.hit_last:#all(all(b== "-" for b in i) for i in self.user_client):
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            if self.user_server_side[x][y] == "*":
                print "YOU GOT HIT!"
                self.hit = True
                self.hit_last = True

                self.user_client[x][y] = "*"
                self.last_hit.append((x, y))

            else:
                print "ENEMY SHOT MISSED!"
                self.hit = False


        else:


            if len(self.last_hit) == 1:
                if self.opening_count == 0: #test by looking forward
                    x = self.last_hit[0][0]
                    y = self.last_hit[0][1]
                    new_y = 6 if x == 7 else x +1

                    if self.user_server_side[x][new_y] == "*":
                        print "YOU GOT HIT"
                        self.hit = True
                        self.user_client[x][new_y] = "*"
                        self.last_hit.append((x, new_y))

                    else:
                        print "ENEMY SHOT MISSED"
                        self.hit = False
                        self.opening_count += 1

                elif self.opening_count == 1: #look behind
                    x = self.last_hit[0][0]
                    y = self.last_hit[0][1]
                    new_y = y - 1
                    if self.user_server_side[x][new_y] == "*":
                        print "YOU GOT HIT"
                        self.hit = True
                        self.user_client[x][new_y] = "*"
                        self.last_hit.append((x, new_y))

                    else:
                        print "ENEMY SHOT MISSED"
                        self.hit = False
                        self.opening_count += 1

                elif self.opening_count == 2: #look above
                    x = self.last_hit[0][0]
                    y = self.last_hit[0][1]
                    new_x = x - 1

                    if self.user_server_side[new_x][y] == "*":
                        print "YOU GOT HIT"
                        self.hit = True
                        self.user_client[new_x][y] = "*"
                        self.last_hit.append((new_x, y))
                    else:
                        print "ENEMY SHOT MISSED"
                        self.hit = False
                        self.opening_count += 1

                elif self.opening_count == 3: #look below
                    x = self.last_hit[0][0]
                    y = self.last_hit[0][1]
                    new_x = 6 if x == 7 else x + 1

                    if self.user_server_side[new_x][y] == "*":
                        print "YOU GOT HIT"
                        self.hit = True
                        self.user_client[new_x][y] = "*"
                        self.last_hit.append((new_x, y))
                    else:
                        raise IndexError("Issue with algorithm")

            elif len(self.last_hit) > 1:
                if self.try_bottom:
                    if all(i[0] == self.last_hit[0][0] for i in self.last_hit):
                        last = self.last_hit[0]
                        if last[1] > 0:
                            new_y = last[1] - 1
                            x = last[0]
                            if self.user_server_side[x][new_y] == "*":
                                print "YOU GOT HIT"
                                self.hit = True
                                self.user_client[x][new_y] = "*"
                                self.last_hit.append((x, new_y))
                                self.try_bottom = True



                            else:
                                print "ENEMY SHOT MISSED!"

                    elif all(i[1] == self.lasthit[0][1] for i in self.last_hit):
                        last = self.last_hit[0]
                        if last[0] > 0:
                            new_x = last[0] - 1
                            y = last[1]
                            if self.user_server_side[new_x][y] == "*":
                                print "YOU GOT HIT"
                                self.hit = True
                                self.user_client[new_x][y] = "*"
                                self.last_hit.append((new_x, y))
                                self.try_bottom = True

                            else:
                                print "ENEMY SHOT MISSED!"

                elif all(i[0] == self.last_hit[0][0] for i in self.last_hit): #going horizontal
                    last = self.last_hit[-1]
                    if last[1] == 7:
                        new_y = self.last_hit[0][1] - 1
                        x = self.last_hit[0][0]
                        if self.user_server_side[x][new_y] == "*":
                            print "YOU GOT HIT"
                            self.hit = True
                            self.user_client[x][new_y] = "*"
                            self.last_hit.append((x, new_y))

                        else:
                            print "ENEMY SHOT MISSED!"

                    else:
                        new_y = last[1] + 1
                        x = last[0]
                        if self.user_server_side[x][new_y] == "*":
                            print "YOU GOT HIT"
                            self.hit = True
                            self.user_client[x][new_y] = "*"
                            self.last_hit.append((x, new_y))

                        else:
                            print "ENEMY SHOT MISSED"
                            self.try_bottom = True

                elif all(i[1] == self.lasthit[0][1] for i in self.last_hit):
                    last = self.last_hit[-1]
                    if last[0] == 7:
                        new_x = self.last_hit[0][0] - 1
                        y = self.last_hit[0][1]
                        if self.user_server_side[new_x][y] == "*":
                            print "YOU GOT HIT"
                            self.hit = True
                            self.user_client[new_x][y] = "*"
                            self.last_hit.append((new_x, y))

                        else:
                            print "ENEMY SHOT MISSED!"

                    else:
                        new_x = last[0] + 1
                        y = last[1]
                        if self.user_server_side[new_x][y] == "*":
                            print "YOU GOT HIT"
                            self.hit = True
                            self.user_client[new_x][y] = "*"
                            self.last_hit.append((new_x, y))

                        else:
                            print "ENEMY SHOT MISSED!"
                            self.try_bottom = True





    def player_move(self, square): #input in the form B4
        y = self.converter[square[0].upper()]
        x = int(square[1])

        if self.opponent_server_side[x-1][y-1] == "*":
            print "HIT!"
            self.opponent_client_side[x-1][y-1] = "*"
            self.last_user_moves.append((x-1, y-1))
        else:
            print "MISSED"

    def is_sunk(self):
        if self.hit:
            answer = raw_input("Kill shot? (Yes/yes/y) ")
            if answer[0].lower() == "y":
                self.sunk = True

            else:
                pass

        else:
            pass


    def print_opponent_client_side(self):
        '''
        print "  "+' '.join(list(string.ascii_uppercase[:8]))
        for i, a in enumerate(self.opponent_client_side):
            print str(i+1)+" "+' '.join(a)
            '''

        print "     "+'    '.join(list(string.ascii_lowercase[:8]))
        print
        print
        for i, a in enumerate(self.opponent_client_side):
            print str(i+1)+"    "+'    '.join(a)
            print
            print

    def print_user_server_side(self):
        '''
        print "  "+' '.join(list(string.ascii_uppercase[:8]))
        for i, a in enumerate(self.user_server_side):
            print str(i+1)+" "+' '.join(a)
        '''
        print "     "+'    '.join(list(string.ascii_lowercase[:8]))
        print
        print
        for i, a in enumerate(self.user_server_side):
            print str(i+1)+"    "+'    '.join(a)
            print
            print






    def __str__(self):
        return "Welcome to the Battleship game"





game = Battleship()
print game
while game.can_play():

    game.print_opponent_client_side()
    game.print_user_server_side()
    loc = raw_input("Enter your square: ")
    game.player_move(loc)
    game.enemy_sunk()
    game.opponent_move()
    game.is_sunk()
    game.determine_sunk_user()

game.determine_winner()
