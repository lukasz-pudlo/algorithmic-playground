root = {'name': 'Alice', 'children': [{'name': 'Bob', 'children':
                                       [{'name': 'Darya', 'children': []}]}, {'name': 'Caroline',
                                                                              'children': [{'name': 'Eve', 'children': [{'name': 'Gonzalo',
                                                                                                                         'children': []}, {'name': 'Hadassah', 'children': []}]}, {'name': 'Fred', 'children': []}]}]}


def search(node):
    print(' Visiting node ' + node['name'] + '...')
    if len(node['children']) > 0:
        for child in node['children']:
            returnValue = search(child)
            if returnValue != None:
                return returnValue
    print('Checking if ' + node['name'] + ' is 8 letters...')
    if len(node['name']) == 8:
        return node['name']
    return None


print('Found an 8-letter name: ' + str(search(root)))
