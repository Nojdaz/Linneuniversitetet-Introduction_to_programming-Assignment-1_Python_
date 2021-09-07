import random


sum = 0
rnglist = []
for x in range(0, 5):
    rng = random.randint(1, 100)
    rnglist.insert(x, rng)
    sum = sum + rng

print("Five random numbers:", rnglist, "\n")
print("The sum is:", sum)



