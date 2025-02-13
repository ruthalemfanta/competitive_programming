from fractions import Fraction

def fractionAddition(expression):
    result = Fraction(0, 1)
    i = 0
    while i < len(expression):
        j = i + 1
        while j < len(expression) and expression[j] != '+' and expression[j] != '-':
            j += 1
        result += Fraction(expression[i:j])
        i = j
    return str(result.numerator) + '/' + str(result.denominator)


expression = "-1/2+1/2"
print(fractionAddition(expression))