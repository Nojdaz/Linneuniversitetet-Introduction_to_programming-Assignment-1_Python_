def nameShorterner():
    firstName = input("First name: ")
    lastName = input("Last name: ")
    print("First name: " + firstName)
    print("Last name: " + lastName)

    return(firstName[0].capitalize() + ". " + lastName[0].capitalize() + lastName[1:4])


while True:
    if __name__ == "__main__":
        print(nameShorterner())
