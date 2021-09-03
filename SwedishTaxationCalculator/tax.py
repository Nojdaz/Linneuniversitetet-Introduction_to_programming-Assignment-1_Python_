income = int(input("Please provide monthly income:"))

#This functions is responsible for calculating the tax it reqiers a int to properly execute
def taxCalc(_income):

    
    if _income < 38000:
        addtax = _income * 0.7
        sum = addtax

    elif _income > 38000 and _income < 50000:
        addtax = _income - 38000
        part1 = (_income - addtax) * 0.7
        part2 = addtax * 0.65
        sum = part1 + part2
    
    elif _income > 50000:
        addtax2 = _income - 50000
        addtax = _income - addtax2 - 38000 
        part1 = (_income - addtax - addtax2) * 0.70
        part2 = addtax * 0.65
        part3 = addtax2 * 0.60
        sum = part1 + part2 + part3
        print(part1,part2,part3)
    
    return sum

print(taxCalc(income))

