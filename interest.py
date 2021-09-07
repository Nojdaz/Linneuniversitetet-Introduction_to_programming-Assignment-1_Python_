savings = int(input("Enter your initial savings: "))
percentage = float(input("Enter your interest rate (in procent): "))

percentage *= 0.01
for i in range(0, 5):
    savings = savings + savings * percentage

print("The value of your savings after 5 years is:", str(savings))