# def ackermann(m, n):
#     if m == 0:
#         return n + 1
#     elif n == 0:
#         return ackermann(m - 1, 1)
#     elif n > 0:
#         return ackermann(m - 1, ackermann(m, n - 1))


# print(ackermann(1, 2))

def ackermann(m, n, indentation=None):
    if indentation is None:
        indentation = 0
    print('%sackermann(%s, %s)' % (' ' * indentation, m, n))

    if m == 0:
        # BASE CASE
        return n + 1
    elif m > 0 and n == 0:
        # RECURSIVE CASE
        return ackermann(m - 1, 1, indentation + 1)
    elif m > 0 and n > 0:
        # RECURSIVE CASE
        return ackermann(m - 1, ackermann(m, n - 1, indentation + 1), indentation + 1)


print(ackermann(4, 2))
