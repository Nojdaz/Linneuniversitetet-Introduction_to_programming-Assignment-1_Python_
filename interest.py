savings = input("Enter your initial savings: ")
percentage = input("Enter your interest rate (in procent): ")

for i in range(0, 5):
    savings = savings + savings * percentage

print("The value of your savings after 5 years is: " + savings)
