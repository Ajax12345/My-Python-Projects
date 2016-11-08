#Schedule Master 2.0
import random
MC = [line.strip() for line in open("/Users/davidpetullo/Documents/MCs.txt", 'r')] #All the preceding files are txt, although csv can also be used. Please email the designer for a release of csv-compatible program
Thurifers = [line.strip() for line in open("/Users/davidpetullo/Documents/Thurifers.txt", 'r')]
Acolytes =  [line.strip() for line in open("/Users/davidpetullo/Documents/Acolytes.txt", 'r')]
BB = [line.strip() for line in open("/Users/davidpetullo/Documents/BBs.txt", 'r')]
CB = [line.strip() for line in open("/Users/davidpetullo/Documents/CBs.txt", 'r')]
backups = [line.strip() for line in open("/Users/davidpetullo/Documents/Backups.txt", 'r')]
print("===============================================================================")
print("Welcome to Schedule Master 2.0. This the second version of the original assignment program. Please note that the 11:00 AM Mass feature is still a work in progress and may not assign new servers every time. This program is runable on python 3 only")
print("This program is for offical Knights Of The Altar use only.")
print("===============================================================================")
ans = int(input("Enter the number of Sundays you would like to schedule for i.e 7: "))
for i in range(ans):
    x = random.sample(MC, 1)
    y = random.sample(Thurifers, 1)
    z = random.sample(Acolytes, 1)
    k = random.sample(Acolytes, 1)
    w = random.sample(BB, 1)
    t = random.sample(CB, 1)
    l = random.sample(backups, 1)

    print("--------------------------")
    print("Week ", i+1)
    print("For The 9:30 AM: \n")
    #the preceding conditional statements verify that servers are not being assigned multiple positions in the same Mass.
    if x == y:
        print("MC: ", "Fred", "\n")
        print("Th: ", y, "\n")
        print("AC1: ", z, "\n")
        print("AC2: ", l, "\n")
        print("BB: ", w, "\n")
        print("CB: ", t, "\n")

    elif y == z:
        print("MC: ", x, "\n")
        print("Th: ", y, "\n")
        print("AC1: ", l, "\n")
        print("AC2: ", k, "\n")
        print("BB: ", w, "\n")
        print("CB: ", t, "\n")


    elif z == w:
        print("MC: ", x, "\n")
        print("Th: ", y, "\n")
        print("AC1: ", z, "\n")
        print("AC2: ", k, "\n")
        print("BB: ", l, "\n")
        print("CB: ", t, "\n")

    elif k == w:
        print("MC: ", x, "\n")
        print("Th: ", y, "\n")
        print("AC1: ", z, "\n")
        print("AC2: ", l, "\n")
        print("BB: ", w, "\n")
        print("CB: ", t, "\n")


    elif z == t:
        print("MC: ", x, "\n")
        print("Th: ", y, "\n")
        print("AC1: ", t, "\n")
        print("AC2: ", k, "\n")
        print("BB: ", w, "\n")
        print("CB: ", l, "\n")



    elif z == k:
        print("MC: ", x, "\n")
        print("Th: ", y, "\n")
        print("AC1: ", w, "\n")
        print ("AC2: ", k, "\n")
        print("BB: ", l, "\n")
        print("CB: ", t, "\n")

    elif w == t:
        print("MC: ", x, "\n")
        print("Th: ", y, "\n")
        print("AC1: ", z, "\n")
        print("AC2: ", k, "\n")
        print("BB: ", w, "\n")
        print("CB: ", 'Karl', "\n")

    else:
        print("MC: ", x, "\n")
        print("Th: ", y, "\n")
        print("AC1: ", z, "\n")
        print("AC2: ", k, "\n")
        print("BB: ", w, "\n")
        print("CB: ", t, "\n")




    print("For the 11:00 AM: \n")

    list = [MC, Thurifers, Acolytes, BB, CB, backups]
    x = random.sample(list, 1)
    for i in x:
        b = random.sample(i, 1)
        v = random.sample(i, 1)
        if b == v:
            print("AC1: James \n")
            print("AC2: Joe \n")
        else:
            print("AC1: ", b, "\n")
            print("AC1: ", v, "\n")
    print("----------------------------")
