#monte hall problem

import random
import matplotlib.pyplot as plt
xs = [i for i in range(1000)]
staying = []
choose_again = []
staying_total = 0
choose_again_total = 0
the_posibilites = ['car', 'goat', 'goat']
for i in range(1000):
    player_choice = random.choice(the_posibilites)
    new_possibilities = ['car', 'goat']
    if player_choice == 'car':
        staying_total += 1

        staying.append(staying_total)

    else:
        staying_total -= 1
        staying.append(staying_total)

for i in range(1000):
    other_player_choice = random.choice(the_posibilites)
    the_new_posibilities = ['car', 'goat']
    switching_value = random.choice(the_new_posibilities)
    if switching_value == 'car':
        choose_again_total += 1

        choose_again.append(choose_again_total)

    else:
        choose_again_total -= 1

        choose_again.append(choose_again_total)

plt.plot(xs, staying)
plt.plot(xs, choose_again)
plt.legend(["Staying", "choosing again"], loc=3)
plt.savefig("Monty_Hall_Simulation.jpeg")
plt.show()
