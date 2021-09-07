income = int(input("Please provide monthly income:"))

if income <= 38000:
    marginalTax = income * 0.7
    sum = marginalTax

elif income > 38000 and income < 50000:
    marginaltax = income - 38000
    taxBracket1 = (income - marginaltax) * 0.7
    taxBracket2 = marginaltax * 0.65
    sum = taxBracket1 + taxBracket2

else:
    marginalTax2 = income - 50000
    marginalTax = income - marginalTax2 - 38000
    taxBracket1 = (income - marginalTax - marginalTax2) * 0.70
    taxBracket2 = marginalTax * 0.65
    taxBracket3 = marginalTax2 * 0.60
    sum = taxBracket1 + taxBracket2 + taxBracket3

print(sum)
