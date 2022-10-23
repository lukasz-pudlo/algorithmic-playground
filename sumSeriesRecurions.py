def sumSeriesByRecursion(n):
    if n == 1:
        return 1
    else:
        return sumSeriesByRecursion(n-1) + n


print(sumSeriesByRecursion(4))
