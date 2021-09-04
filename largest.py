
def findlargerst(listOfNumbers):
    i = listOfNumbers[0]
    for x in listOfNumbers:
        if x >= i:
            i = x
        else:
            continue
    return i

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

listnumbers = [A,B,C]
print(findlargerst(listnumbers))
