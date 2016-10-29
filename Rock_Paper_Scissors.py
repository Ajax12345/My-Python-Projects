while True:
    player1 = raw_input("Enter rock, paper, or scissors: ")
    player2 = raw_input("Enter rock, paper, or scissors: ")
    if player1 == 'rock' and player2 == 'paper':
        print "Player2 wins"

    elif player1 == 'paper' and player2 == 'scissors':
        print "Player2 wins"

    elif player1 == 'scissors' and player2 == 'paper':
        print "Player1 wins"

    elif player1 == 'paper' and player2 == 'rock':
        print "Player1 wins"

    elif player1 == 'scissors' and player2 == 'rock':
        print "Player2 wins"

    elif player1 == 'rock' and player2 == 'scissors':
        print "Player1 wins"

    elif player1 == 'paper' and player2 == 'rock':
        print "Player1 wins"

    elif player1 == 'paper' and player2 == 'paper':
        print "tie"

    elif player1 == 'rock' and player2 == 'rock':
        print "tie"

    elif player1 == 'scissors' and player2 == 'scissors':
        print "tie"

    ans = raw_input("Do you want to play again? ")
    if ans == 'y' or ans == 'Y' or ans == 'Yes' or ans == 'yes':
        continue
    else:
        print "Thank you for playing"
        break
