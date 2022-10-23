def concat(elements):
    if len(elements) == 0:
        return ''
    else:
        head = elements[0]
        tail = elements[1:]
        return head + concat(tail)


elements = ['mouse ', 'has ', 'been ', 'caught']

print(concat(elements))
