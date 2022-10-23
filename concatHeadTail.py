def concat(stringToConcat):
    if len(stringToConcat) == 1:
        return stringToConcat[0]
    else:
        head = stringToConcat[0]
        tail = stringToConcat[1:]
        return head + concat(tail)


print(concat(['Hello', 'World']))
