def product(integers):
    if len(integers) == 0:
        return 1
    elif len(integers) == 1:
        return integers[0]
    else:
        head = integers[0]
        tail = integers[1:]
        return head * product(tail)


print(product([4232, 23, 898983498349843, 12391031, 1290129, 192102]))
