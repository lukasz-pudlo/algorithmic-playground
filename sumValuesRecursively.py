def sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return sum(numbers[:len(numbers)-1]) + numbers[-1]


print(sum([1, 2, 3]))
