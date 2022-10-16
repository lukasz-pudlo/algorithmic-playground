from tkinter import N


from showcallstack import showcallstack


def factorial(n, recursiveCallCounter, baseCaseCounter):
    print(n)
    if n == 1:
        baseCaseCounter += 1
        print('base case counter is currently %s' % baseCaseCounter)
        return 1
    else:
        recursiveCallCounter += 1
        recursiveCall = factorial(
            n - 1, recursiveCallCounter, baseCaseCounter) * n
        print('the recursive call %s is currently %s' %
              (recursiveCallCounter, recursiveCall))
        return recursiveCall


print(factorial(8, 0, 0))
