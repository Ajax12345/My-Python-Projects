import copy
import random
import pygame
import time
class Cube:
    def __init__(self):
        self.cube = [['w', 'w', 'w'], [['y', 'y', 'y'], ['y', 'y', 'y']], [['r', 'r', 'r'], ['r', 'r', 'r']], ['o', 'o', 'o']]
        '''
        ['w', 'w', 'w']
        ---------------
        ['y', 'y', 'y']
        ['y', 'y', 'y']
        ---------------
        ['r', 'r', 'r']
        ['r', 'r', 'r']
        --------------
        ['o', 'o', 'o']

        '''
        self.benchmark = [['w', 'w', 'w'], [['y', 'y', 'y'], ['y', 'y', 'y']], [['r', 'r', 'r'], ['r', 'r', 'r']], ['o', 'o', 'o']]
        self.moves = {"twist_top_1":self.twist_top_1, "twist_top_2":self.twist_top_2, "twist_upper":self.twist_upper, "twist_middle":self.twist_middle, "twist_bottom":self.twist_lower}
    def is_finished(self, cube):
        #TODO:test if unpacking is actually necessary

        side1, [top1, top2], [bottom1, bottom2], side2 = cube
        s1, [t1, t2], [b1, b2], s2 = self.benchmark

        return all(a==b for a, b in zip(cube, self.benchmark))


    def scramble(self):
        while True:
            for i in range(5):
                move = random.choice(self.moves.keys())
                print move
                self.cube = self.moves[move](self.cube)

            if not self.is_finished(self.cube):
                break

    def scramble1(self):
        new_cube = copy.deepcopy(self.cube)
        while True:
            for i in range(5):
                move = random.choice(self.moves.keys())

                new_cube = self.moves[move](new_cube)

            if not self.is_finished(new_cube):
                break

        return new_cube

    def solve1(self, cube):

        while True:
            new_cube = copy.deepcopy(cube)
            move = random.choice(self.moves.keys())
            new_cube = self.moves[move](new_cube)
            moves = [move]
            finished = False
            for i in range(5):
                new_move = random.choice(self.moves.keys())
                moves.append(new_move)
                new_cube = self.moves[new_move](new_cube)
                temp_flag = False
                if self.is_finished(new_cube):

                    finished = True
                    break


                else:
                    for the_move in self.moves:
                        final_copy_cube = self.moves[the_move](copy.deepcopy(new_cube))

                        if self.is_finished(final_copy_cube):
                            #print "final_copy_cube", final_copy_cube
                            moves.append(the_move)
                            finished = True
                            temp_flag = True
                            break
                if temp_flag:
                    break

            if finished:
                return moves
                break


    def solve(self):

        while True:
            new_cube = copy.deepcopy(self.cube)
            move = random.choice(self.moves.keys())
            new_cube = self.moves[move](new_cube)
            moves = [move]
            finished = False
            for i in range(5):
                new_move = random.choice(self.moves.keys())
                moves.append(new_move)
                new_cube = self.moves[new_move](new_cube)
                temp_flag = False
                if self.is_finished(new_cube):

                    finished = True
                    break


                else:
                    for the_move in self.moves:
                        final_copy_cube = self.moves[the_move](copy.deepcopy(new_cube))

                        if self.is_finished(final_copy_cube):
                            #print "final_copy_cube", final_copy_cube
                            moves.append(the_move)
                            finished = True
                            temp_flag = True
                            break
                if temp_flag:
                    break

            if finished:
                return moves
                break







    def twist_top_1(self, cube):
        first_side = cube[1][1]
        second_side = cube[2][1]
        cube[1][1] = second_side[::-1]
        cube[2][1] = first_side[::-1]

        cube[-1] = cube[-1][::-1]
        return cube


    def twist_top_2(self, cube):
        first_side = cube[1][0]
        second_side = cube[2][0]
        cube[1][0] = second_side[::-1]
        cube[2][0] = first_side[::-1]
        cube[0] = cube[0][::-1]
        return cube

    def twist_upper(self, cube):
        first = zip(*cube[1])
        second = zip(*cube[2])
        top1 = first[-1]
        top2 = second[-1]
        first[-1] = top2
        second[-1] = top1
        cube[1] = zip(*first)
        cube[2] = zip(*second)
        top_corner = cube[0][-1]
        top_corner1 = cube[-1][-1]
        cube[0][-1] = top_corner1
        cube[-1][-1] = top_corner
        return [map(list, i) if all(isinstance(b, tuple) for b in i) else i for i in cube]

    def twist_middle(self, cube):
        first = zip(*cube[1])
        second = zip(*cube[2])
        middle1 = first[1]
        middle2 = second[1]
        first[1] = middle2
        second[1] = middle1
        middle_side1 = cube[0][1]
        middle_side2 = cube[-1][1]
        cube[0][1] = middle_side2
        cube[-1][1] = middle_side1
        cube[1] = map(list, zip(*first))
        cube[2] = map(list, zip(*second))
        return cube

    def twist_lower(self, cube):
        first = zip(*cube[1])
        second = zip(*cube[2])
        middle1 = first[0]
        middle2 = second[0]
        first[0] = middle2
        second[0] = middle1
        middle_side1 = cube[0][0]
        middle_side2 = cube[-1][0]
        cube[0][0] = middle_side2
        cube[-1][0] = middle_side1
        cube[1] = map(list, zip(*first))
        cube[2] = map(list, zip(*second))
        return cube

class VisualCube(Cube):
    def __init__(self):

        Cube.__init__(self)

        self.screen = pygame.display.set_mode((1000, 900))
        self.keep_running = True
        self.scrambled_cube = None
        self.the_moves = []
        self.clockobject = pygame.time.Clock()
        self.game_time = 0
        self.index_so_far = 0
        self.new_scrambled_cube = None

    def solve_puzzle(self):
        self.scrambled_cube = self.scramble1()


        self.new_scrambled_cube = copy.deepcopy(self.scrambled_cube)

        self.the_moves = self.solve1(self.scrambled_cube)
        print self.the_moves


        self.show_cube()
    def draw_generic_cube(self, cube_now):
        table = {"w":(255, 255, 255), "o":(255, 165, 0), "r":(255, 0, 0), "y":(255, 255, 0)}
        side_distance = 100
        seen_side_1 = False
        seen_front_1 = False
        x = 500
        y = 500
        z = 500
        x1 = 0
        y1 = 0
        z1 = 500

        for face in cube_now:
            if not all(isinstance(b, list) for b in face):
                if seen_side_1:
                    for c in face:

                        pygame.draw.rect(self.screen, table[c], (300, x, 60, 60)) #100
                        x += 60
                        #x1 += 60

                else:
                    seen_side_1 = True
                    for c in face:
                        pygame.draw.rect(self.screen, table[c], (700, y, 60, 60)) # 500

                        y += 60

            else:
                if seen_front_1:
                    for side in face:

                        for color in side:
                            pygame.draw.rect(self.screen, table[color], (600, z, 60, 60)) #400
                            z += 60

                else:
                    seen_front_1 = True
                    for side in face:
                        for color in side:
                            pygame.draw.rect(self.screen, table[color], (400, z1, 60, 60)) #400
                            z1 += 60

    def draw_cube(self):
        table = {"w":(255, 255, 255), "o":(255, 165, 0), "r":(255, 0, 0), "y":(255, 255, 0)}
        side_distance = 100
        seen_side_1 = False
        seen_front_1 = False
        x = 100
        y = 100
        z = 100
        x1 = 0
        y1 = 0
        z1 = 100

        for face in self.scrambled_cube:
            if not all(isinstance(b, list) for b in face):
                if seen_side_1:
                    for c in face:

                        pygame.draw.rect(self.screen, table[c], (300, x, 60, 60)) #100
                        x += 60
                        #x1 += 60

                else:
                    seen_side_1 = True
                    for c in face:
                        pygame.draw.rect(self.screen, table[c], (700, y, 60, 60)) # 500

                        y += 60

            else:
                if seen_front_1:
                    for side in face:

                        for color in side:
                            pygame.draw.rect(self.screen, table[color], (600, z, 60, 60)) #400
                            z += 60

                else:
                    seen_front_1 = True
                    for side in face:
                        for color in side:
                            pygame.draw.rect(self.screen, table[color], (400, z1, 60, 60)) #400
                            z1 += 60


        try:
            self.the_current_move = self.the_moves[self.index_so_far]

                #print self.move
                #print move
            self.new_scrambled_cube = self.moves[self.the_current_move](self.new_scrambled_cube)

                #print self.new_scrambled_cube
                #time.sleep(1)
            self.draw_generic_cube(self.new_scrambled_cube)

        except:
            #self.new_scrambled_cube = self.moves[self.the_moves[-1]](self.new_scrambled_cube)
            self.draw_generic_cube(self.new_scrambled_cube)









    def show_cube(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 900))
        #self.clockobject.tick(60)
        while self.keep_running:
            #self.clockobject.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.alive = False

            #self.draw_cube()



            self.game_time += 1
            if self.game_time%1000 == 0:

                self.index_so_far += 1

            self.draw_cube()


            pygame.display.flip()



        pygame.quit()




if __name__ == "__main__":

    c = Cube()
    print c.moves["twist_middle"](c.cube)
    '''
    c.scramble()
    for i in c.cube:
        print i

    moves = c.solve()
    print moves
    for move in moves:
        c.cube = c.moves[move](c.cube)

    for i in c.cube:
        print i
    '''



    '''
    c = VisualCube()

    c.solve_puzzle()
    '''
