amount = int(input("Enter the amount you have budgeted for this month: "))
value = 0
while True:
    x = int(input("Enter you expenses one at a time: "))
    value = value + x
    ans = input("Do you have more to enter? ")
    if ans == 'y' or ans == 'Y' or ans == 'yes' or ans == 'Yes':
        continue

    else:
        break

test = amount - value
if test >= 0:
    print("Nice job. You spent within you budget")

else:
    print("You spent above your set budget for this month")
