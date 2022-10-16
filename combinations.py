from showcallstack import showcallstack


def powerset(array):
    # Write your code here.

    combinations = [[]]
    helper(0, array, combinations)
    result = []
    [result.append(x) for x in combinations if x not in result]
    result.sort(key=len)
    result.sort()
    print(result)


def helper(idx, array, combinations):
    if len(array) == 0:
        return combinations
    elif len(array) == 1:
        combinations.append(array)
    else:
        combinations.append(array)
        showcallstack()
        for element in array:
            combinations.append([element])

        while idx < len(array) - 1:
            idx += 1
            helper(idx, array[idx:], combinations)
            for index, element in enumerate(array):
                if array[index] != array[0]:
                    combination = [array[0], array[index]]
                    combinations.append(combination)


array = [1, 2, 3, 4, 5]


powerset(array)
