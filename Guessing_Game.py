import random
x = random.randint(1, 10)
print "I am thinking of a number"
while True:
    while True:
        y = input("Enter your guess between 1 and 10: ")
        if x != y:
            print "Wrong guess, try again"
            continue
        else:
            print "You guessed correctly!"
            break

            print "Thank you for playing"

    ans = raw_input("Do you want to play again?")
    if ans == 'y' or ans == 'Y' or ans == 'Yes' or ans == 'yes':
        continue

    else:
        break

print "Come back soon!!"
