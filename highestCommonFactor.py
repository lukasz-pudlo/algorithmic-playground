from json.encoder import INFINITY


def highestCommonFactor(a, n):
    q = INFINITY
    r = INFINITY
    lastR = INFINITY
    if a % n == 0:
        print('a can be divided by n without a remainder, which means that the highst common factor is in fact n, that is', n)
        return n
    else:
        while True:
            print('At this stage a is', a, 'and n is', n)
            print('And at this stage q is', q, 'and r is',
                  r, 'and of course last r is', lastR)
            q = a // n
            print('q is', q)
            r = a - (q * n)
            print('r is', r)
            if r == 0:
                break
            lastR = r
            print('Last r is', lastR)
            print('The equation at this stage is', a, '=', q, '*', n, '+', r)
            a = n
            print('Now a is', a)
            n = r
            print('Now n is', n)
        print('Last r is', lastR, 'which should be the result')
        return lastR


print(highestCommonFactor(81, 27))
