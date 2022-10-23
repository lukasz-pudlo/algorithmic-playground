def sumPowersOf2Recursive(n):
    if n == 1:
        return 2
    else:
        return sumPowersOf2Recursive(n - 1) + 2 ** n


print(sumPowersOf2Recursive(4))
