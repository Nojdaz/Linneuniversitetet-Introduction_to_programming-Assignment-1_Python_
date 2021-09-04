import random

def oddPositive():
    rng = random.randint(-10,10)
    if rng >= 0:
        print(rng,"is a positive number")
    else:
        print(rng, "is negative")
    if rng % 2 == 0:
        print(rng," is an even number")
    else: 
        print(rng," is an odd number")

while True:
    if __name__ == "__main__":
        print(oddPositive())