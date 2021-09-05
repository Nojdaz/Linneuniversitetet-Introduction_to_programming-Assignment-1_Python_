def squareCalc(coordinate):
    if (ord(coordinate[0])) % 2 == int(coordinate[1]) % 2:
        return "Black"

    else:
        return "White"


coordinate = input("Enter a chess square identifier (e.g. e5):")
print(squareCalc(coordinate))
