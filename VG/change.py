price = float(input("Enter the price"))
payment = float(input("Enter how much you payed"))

if price > payment:
    print("You don't have enough for this purchase")
else:
    change = payment - price
    change = round(change, 2)
    print("Price:", price)
    print("Payment:", payment)
    print("")
    print("Change:", change)
    print("1000kr bills:", change // 1000)
    change %= 1000
    print("500kr bills:", change // 500)
    change %= 500
    print("200kr bills:", change // 200)
    change %= 200
    print("100kr bills:", change // 100)
    change %= 100
    print("50kr bills:", change // 50)
    change %= 50
    print("20kr bills:", change // 20)
    change %= 20
    print("10kr coins:", change // 10)
    change %= 10
    print("5kr coins:", change // 5)
    change %= 5
    print("2kr coins:", change // 2)
    change %= 2
    print("1kr coins:", change // 1)
    change %= 1
