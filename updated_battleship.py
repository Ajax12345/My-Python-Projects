import random
class HeadQuarters:
  def __init__(self):
    self.player1 = [["*" for i in range(6)] for b in range(6)]
    self.player2 = [["*" for i in range(6)] for b in range(6)]
    self.data1= [["*", '*', '*','*', '*', '*'],
                 ["*", '*', '*','*', '*', '*'],
                 ["*", '*', '*','*', '*', '*'],
                 ["*", '*', '*','*', '*', '*'],
                 ["*", '*', '*','*', '*', '*'],
                 ["*", '*', '*','*', '*', '*']]

    self.data2 = [["*", '*', '*','*', '*', '*'],
                  ["*", '*', '*','*', '*', '*'],
                  ["*", '*', '*','*', '*', '*'],
                  ["*", '*', '*','*', '*', '*'],
                  ["*", '*', '*','*', '*', '*'],
                  ["*", '*', '*','*', '*', '*']]

    self.battleship1 = [[(0, 0), (1, 0), (2, 0)], [(1, 2), (1, 3), (1, 4), (1, 5)]]

    self.battleship2 = [[(2, 0), (2, 1), (2, 2)], [(1, 2), (1, 3), (1, 4), (1, 5)]]

    self.battleship_class = {3:"Patrol Boat", 4:"destroyer"}

    self.successful_move = []

  def move1(self, x, y):
    if self.player2[x-1][y-1] == '#':
      self.data1[x-1][y-1] = '#'
      print "Direct Hit"
      for i in self.battleship2:
        for b in range(len(i)):
          if i[b] == (x-1, y-1):
            i[b] = True


    else:
      print "Miss"



  def initial_move1(self):
    x = random.randint(0, 6)
    y = random.randint(0, 6)
    if self.player1[x-1][y-1] == '#':
      self.data2[x-1][y-1] = '#'
      print "Direct Hit"
      self.successful_move = [x-1, y-1]
      for i in self.battleship1:
        for b in range(len(i)):
          if i[b] == (x-1, y-1):
            i[b] = True

  def move2(self):
    if len(self.successful_move) == 0:
        x = random.randint(0, 6)
        y = random.randint(0, 6)
        if self.player1[x-1][y-1] == '#':
            self.data2[x-1][y-1] = '#'
            print "Direct Hit"
            self.successful_move = [x-1, y-1]
            for i in self.battleship1:
                for b in range(len(i)):
                    if i[b] == (x-1, y-1):
                        i[b] = True

    else:
        self.options = {"up":True, "down":True, "left":True, "right":True}
        if self.successful_move[1] > 1:
            self.options["down"] = True

        else:
            self.options["down"] = False
        if len(self.data1[0]) - self.successful_move[0] > 1:
            self.options["right"] = True

        else:
            self.options["right"] = False
        if self.successful_move[0] > 1:
            self.options["left"] = True
        else:
            self.options["left"] = False

        if self.successful_move[1] < len(self.data1)-1:
            self.options["up"] = True
        else:
            self.options["up"] = False

        self.moves = [a for a, b in self.options.items() if b]
        self.the_move = self.moves[0]
        if self.the_move == "up":
            self.cord = [self.successful_move[0], self.successful_move[1]+1]
            if self.player1[self.cord[0]][self.cord[1]] == "#":
                self.data2[self.cord[0]][self.cord[1]] = '#'
                print "Direct Hit"
                self.successful_move = [self.cord[0], self.cord[1]]
                for i in self.battleship1:
                    for b in range(len(i)):
                        if i[b] == (self.cord[0], self.cord[1]):
                            i[b] = True




  def checker1(self):

     if all(i == True for i in self.battleship2):
        print "enemy ", self.battleship_class[len(i)], " sunk! Nice work commander!"

  def checker2(self):

     if all(i== True for i in self.battleship1):
        print "Commander! You have lost a ", self.battleship_class[len(i)]

  def shipsetter1(self):
    for i in self.battleship1:
      for b in i:
        self.data1[list(b)[0]][list(b)[1]] = '#'

  def shipsetter2(self):
    for i in self.battleship2:
      for b in i:
        self.data2[list(b)[0]][list(b)[1]] = '#'

  def show(self):
    for i in self.data1:
      for b in i:
        print b,

      print

    print

battle = HeadQuarters()

battle.shipsetter1()
battle.shipsetter2()
battle.show()

print "the game begins"
x = input("Enter the x-cordinate: ")
y = input("Enter the y-coordinate: ")
battle.move1(x, y)
battle.initial_move1()
for i in range(10):
    x = input("Enter the x-cordinate: ")
    y = input("Enter the y-coordinate: ")
    battle.move1(x, y)
    battle.checker1()
    battle.show()
    battle.move2()
    battle.checker2()
