import random

def rngGenerator():
    sum = 0
    rnglist = []
    for x in range(0, 5):
        rng = random.randint(1, 100)
        rnglist.insert(x,rng)
        sum = sum + rng
    return sum, rnglist

int, array = rngGenerator()
print("Five random numbers:",array,"\n")
print("The sum is:", int)



