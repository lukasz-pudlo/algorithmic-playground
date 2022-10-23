# def reverseString(letters):
#     if len(letters) == 0:
#         return ''
#     elif len(letters) == 1:
#         return letters[0]
#     else:
#         head = letters[-1]
#         tail = letters[:-1]
#         return head + reverseString(tail)

def reverseString(letters):
    if len(letters) == 0:
        return ''
    elif len(letters) == 1:
        return letters[0]
    else:
        head = letters[0]
        tail = letters[1:]
        return reverseString(tail) + head


elements = ['a', 'b', 'c']

print(reverseString('Hello world, hi there'))
