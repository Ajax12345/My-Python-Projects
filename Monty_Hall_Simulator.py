import random
import matplotlib.pyplot as plt

success = 0
failure = 0
successes = []
failures = []
for i in range(100):
    options = ["car", "goat", "goat"]
    player_choice = random.choice(options)
    options.remove("goat")
    options.remove(player_choice)
    for i in options:
        if i == "car":
            success += 1
            successes.append(success)


        else:
            failure += 1
            failures.append(failure)
print "The success out of 100 when switching your option is ", success
print "The success out of 100 when staying with your initial choice is ", failure


plt.hist([successes, failures])
plt.legend(["Switching", "Staying"])
plt.xlabel("Cars or Goats")
plt.title("Monty Hall Problem")
plt.show()
