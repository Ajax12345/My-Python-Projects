while True:
    x = input("Enter a number to see if it is prime: ")
    if x == 1 or x == 0:
        print x, "is niether prime nor composite"

    elif x > 1:
       
        if all(x%i !=0 for i in range(2, x)):
            print x, "is prime"
            
        else:
            print x, "is not prime"

    ans = raw_input("do you want to play again?")
    if ans == 'y' or ans == 'Yes' or ans == 'yes':
        continue

    else:
        print "Thank you for playing"
        break
        
