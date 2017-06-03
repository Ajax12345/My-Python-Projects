#uberbot 3

def parkingSpot(carDimensions, parkingLot, luckySpot):

    new_board = map(list, zip(*parkingLot))
    flag1 = all(i == 0 for i in new_board[0][luckySpot[1]:luckySpot[1]+carDimensions[1]]) #front
    flag2 = all(i == 0 for i in new_board[-1][luckySpot[1]:luckySpot[1]+carDimensions[1]]) #back
    flag3 = all(i == 0 for i in parkingLot[0][luckySpot[0]+1:carDimensions[0]]) #top of lot
    flag4 = all(i == 0 for i in parkingLot[-1][luckySpot[0]+1:carDimensions[0]]) #bottom of lot

    print flag1
    print flag2
    print flag3
    print flag4
    print "_________"

    if flag1:
        counter_list = []
        parking_matrix = []
        print "are we here"
        for i in new_board[luckySpot[0]:luckySpot[3]+1]:
            print i[luckySpot[1]:luckySpot[2]+1]
            parking_matrix.append(i[luckySpot[1]:luckySpot[2]+1])

            if all(b == 0 for b in i[luckySpot[1]:luckySpot[2]+1]):
                counter_list.append(True)



        if all(counter_list):


            return True



        else:
            return False


    elif flag2:
        counter_list = []
        parking_matrix = []
        print "at number 2"
        for i in new_board[::-1][luckySpot[0]:luckySpot[3]+1]:
            #print i[luckySpot[1]:luckySpot[2]+1]
            parking_matrix.append(i[luckySpot[1]:luckySpot[2]+1])

            if all(b == 0 for b in i[luckySpot[1]:luckySpot[2]+1]):
                counter_list.append(True)

        car_width = [[0]*carDimensions[1]]*carDimensions[0]

        print car_width
        print parking_matrix

        if all(counter_list):
            return True

        else:
            return False

    elif flag3:
        counter_list = []
        parking_matrix = [] #this stores the spot created
        #have a function to check returned matrix
        print "trying here"
        for i in parkingLot[luckySpot[0]:luckySpot[2]+1]:
            print i[luckySpot[1]:luckySpot[3]+1]
            parking_matrix.append(i[luckySpot[0]:luckySpot[3]+1])
            if all(b == 0 for b in i[luckySpot[1]:luckySpot[3]+1]):
                counter_list.append(True)

            else:
                counter_list.append(False)

        print [[0]*carDimensions[1]]*carDimensions[0]

        if all(counter_list):
            if len(parking_matrix) >= len([[0]*carDimensions[1]]*carDimensions[0]):

                return True
            else:
                return False


        else:
            return False

    elif flag4:
        print "here"
        counter_list = []
        parking_matrix = [] #this stores the spot created
        #have a function to check returned matrix
        for i in parkingLot[::-1][luckySpot[1]:luckySpot[2]+1]: #may need to change to [luckySpot[0]:luckySpot[2]+1]
            print i[luckySpot[0]:luckySpot[3]+1]
            parking_matrix.append(i[luckySpot[0]:luckySpot[3]+1])
            if all(b == 0 for b in i[luckySpot[0]:luckySpot[3]+1]):
                counter_list.append(True)

            else:
                counter_list.append(False)

        if all(counter_list):
            if len(parking_matrix) >= len([[0]*carDimensions[1]]*carDimensions[0]):
                return True
            else:
                return False


        else:
            return False

print parkingSpot([3, 2], [[1,0,1,0,1,0],
 [0,0,0,0,1,0],
 [0,0,0,0,0,1],
 [1,0,1,1,1,1]], [1, 1, 2, 3]) #may need to consider x,y; rather than y, x
