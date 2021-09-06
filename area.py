def CalcCircleArea(Radius):
    A = 3.14*float(Radius)**2
    return A


if __name__ == "__main__":
    while True:
        try:
            radius = input("Enter the circle radius: ")
            print("This circles area is:", CalcCircleArea(radius))
        except:
            continue
