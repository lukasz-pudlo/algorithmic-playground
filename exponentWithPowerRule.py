def exponentWithPowerRule(number, exponent):
    opStack = []

    while exponent > 1:
        if exponent % 2 == 0:
            opStack.append('square')
            exponent = exponent // 2
        elif exponent % 2 == 1:
            exponent -= 1
            opStack.append('multiply')

    result = number

    while opStack:
        op = opStack.pop()

        if op == 'square':
            result *= result
        elif op == 'multiply':
            result *= number

    return result


print(exponentWithPowerRule(2, 3))
