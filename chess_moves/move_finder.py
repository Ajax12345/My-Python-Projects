def get_bishop_moves(view_board, x, y):
    to_return = []
    new_y = y
    new_x = x
    while True:

        if new_y +1 < 8 and new_x + 1 < 8:
            #print "got here"
            new_y += 1
            new_x += 1

                #print "got here"
            to_return.append((new_x, new_y))


        else:
            break
    new_y = y
    new_x = x

    while True:

        if new_y - 1 >=0 and new_x - 1 >= 0:
            new_y -= 1
            new_x -= 1
            # or "w" in view_board[new_x][new_y]:
                #print "got here"
            to_return.append((new_x, new_y))

        else:
            break

    new_y = y
    new_x = x

    while True:

        if new_y + 1 < 8 and new_x -1 >= 0:
            new_y += 1
            new_x -= 1
            #or "w" in view_board[new_x][new_y]:
                #print "got here"
            to_return.append((new_x, new_y))




        else:
            break

    new_y = y
    new_x = x

    while True:
        if new_y -1 >= 0 and new_x + 1 < 8:
            new_y -= 1
            new_x += 1

                #print "got here"
            to_return.append((new_x, new_y))



        else:
            break

    return to_return

def get_rook_moves(view_board, x, y):
    to_return = []

    for i in range(1, x):
        a, b = (x-i, y)


        to_return.append((a, b))


    for i in range(x, 8):
        a, b = (i, y)

        to_return.append((a, b))





    for i in range(y, 8):
        a, b = (x, i)

        to_return.append((a, b))


    for i in range(1, y):
        a, b = (x, y-i)

        to_return.append((a, b))


    return to_return



def get_knight_moves(view_board, x, y):
    to_return = []

    try:
        a, b = (x+2, y+1) #-
                              #-
                              #- -
        if view_board[a][b] == "-":
            to_return.append((a, b))

    except:
        pass

    try:
        a, b = (x+2, y-1) #-
                        #-
                        #- -


        if view_board[a][b] == "-":
            to_return.append((a, b))

    except:
        pass

    try:
        a, b = (x+1, y+2) #- - -
                                  #-
        if view_board[a][b] == "-":
            to_return.append((a, b))

    except:
        pass

    try:
        a, b = (x-1, y+2)   #-
                            #- - -
        if a > 0:

            if view_board[a][b] == "-":
                to_return.append((a, b))

    except:
        pass

    try:
        a, b = (x+1, y-2)
        if view_board[a][b] == "-":
            to_return.append((a, b))

    except:
        pass

    try:
        a, b = (x-1, y-2)
        if a > 0:
            if view_board[a][b] == "-":
                to_return.append((a, b))

    except:
        pass

    #return to_return
    return [i for i in to_return if all(b >= 0 for b in i)]

def get_queen_moves(view_board, x, y):

    ranks = get_rook_moves(view_board, x, y)
    diags = get_bishop_moves(view_board, x, y)

    return ranks + diags
