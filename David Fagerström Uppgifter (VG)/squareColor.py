def squareCalc(coordinate):

    if (ord(coordinate[0]) + int(coordinate[1])) % 2:
        return "White"


if __name__ == "__main__":
    while True:
        try:
            coordinate = input("Enter a chess square identifier (e.g. e5):")
            print(squareCalc(coordinate))

        except:
            continue
