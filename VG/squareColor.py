coordinate = input("Enter a chess square identifier (e.g. e5):")

if (ord(coordinate[0]) + int(coordinate[1])) % 2:
    print ("White")

else:
    print("Black")