#this is a recreation of the classic game of Nims and Stones
pile = 100
while pile >=1:
    choice1 = input("Enter player 1's choice, between 1 and 5, inclusive: ")
    pile -= choice1
    print "There are",pile, "stones left"
    if pile < 5 and pile >= 1:
        print "Player one won!!"
        break
    else:
        choice2 = input("Enter player 2's pick: ")
        pile -= choice2
        print "there are", pile, "stones left"
        if pile < 5 and pile >= 1:
            print "Player two won!!"
            break

        else:
            continue
