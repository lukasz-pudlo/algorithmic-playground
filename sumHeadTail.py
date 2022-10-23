from showcallstack import showcallstack


def sum(numbers):
    showcallstack()
    if len(numbers) == 0:
        return 0
    else:
        head = numbers[0]
        tail = numbers[1:]
        return head + sum(tail)


print(sum([67, 980, 3]))
