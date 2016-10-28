number = int(input("Enter you number: "))
factorial = 1
if number == 0:
    print("O factorial is 1")

elif number > 0:
    for i in range(1, number+1):
        factorial = factorial*i

print(number, " factorial is ", factorial)
