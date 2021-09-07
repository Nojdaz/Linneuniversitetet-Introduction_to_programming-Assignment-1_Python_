income = int(input("Please provide monthly income:"))

# This functions is responsible for calculating the tax it reqiers a int to properly execute


def taxBracket1(_income):
    marginalTax = _income * 0.7
    sum = marginalTax
    return sum


def taxBracket2(_income):
    marginaltax = _income - 38000
    taxBracket1 = (_income - marginaltax) * 0.7
    taxBracket2 = marginaltax * 0.65
    sum = taxBracket1 + taxBracket2
    return sum


def taxBracket3(_income):
    marginalTax2 = _income - 50000
    marginalTax = _income - marginalTax2 - 38000
    taxBracket1 = (_income - marginalTax - marginalTax2) * 0.70
    taxBracket2 = marginalTax * 0.65
    taxBracket3 = marginalTax2 * 0.60
    sum = taxBracket1 + taxBracket2 + taxBracket3
    return sum


def taxCalc(income):

    if income <= 38000:
        return taxBracket1(income)

    elif income > 38000 and income < 50000:
        return taxBracket2(income)

    elif income > 50000:
        return taxBracket3(income)


print(taxCalc(income))
