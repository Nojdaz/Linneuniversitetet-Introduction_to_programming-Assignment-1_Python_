def sumOfDigits(threeDigits):
    sum = 0
    for i in range(0, 3):
        sum = sum + int(threeDigits[i])
    return sum


if __name__ == "__main__":
   while True:
        try: 
            threeDigitNumber = input("Enter a three digit number: ")
            print(sumOfDigits(threeDigitNumber))
    
        except:
         continue
