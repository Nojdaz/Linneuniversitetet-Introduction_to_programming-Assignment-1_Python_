A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

listnumbers = [A, B, C]

i = listnumbers[0]
for x in listnumbers:
    if x >= i:
        i = x
    else:
        continue
print(i)
