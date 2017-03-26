x = 167
counter_list = []
for i in range(2, x):
    if x%i != 0:
        counter_list.append(1)

    else:
        break


if len(counter_list) == x-2:
    print "It is prime"

else:
    print "It is not prime"
