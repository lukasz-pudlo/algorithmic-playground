from turtle import goto


def findSubstringIterative(needle, haystack):
    i = 0
    while i < len(haystack):
        if haystack[i:i + len(needle)] == needle:
            return i
        i += 1
    return -1


needle = 'like'
haystack = 'I would like to go somewhere warm'

#print(findSubstringIterative(needle, haystack))


def findSubstringRecursively(needle, haystack, i=0):
    if i >= len(haystack):
        return -1
    elif haystack[i:i + len(needle)] == needle:
        return i
    else:
        return findSubstringRecursively(needle, haystack, i + 1)


print(findSubstringRecursively(needle, haystack))
