from showcallstack import showcallstack

root = {'data': 'A', 'children': []}
node2 = {'data': 'B', 'children': []}
node3 = {'data': 'C', 'children': []}
node4 = {'data': 'D', 'children': []}
node5 = {'data': 'E', 'children': []}
node6 = {'data': 'F', 'children': []}
node7 = {'data': 'G', 'children': []}
node8 = {'data': 'H', 'children': []}

root['children'] = [node2, node3]
node2['children'] = [node4]
node3['children'] = [node5, node6]
node5['children'] = [node7, node8]


def preOrderTraverse(node):
    print(node['data'], end=' ')
    if len(node['children']) > 0:
        for child in node['children']:
            preOrderTraverse(child)
    return


def postOrderTraverse(node):
    for child in node['children']:
        postOrderTraverse(child)
    print(node['data'], end=' ')
    return


def inOrderTraverse(node):
    if len(node['children']) >= 1:
        inOrderTraverse(node['children'][0])
    print(node['data'], end=' ')
    if len(node['children']) >= 2:
        inOrderTraverse(node['children'][1])
    return


# def getDepth(node):
#     # showcallstack()
#     if len(node['children']) == 0:
#         return 0
#     else:
#         maxDepth = 0
#         for child in node['children']:
#             childDepth = getDepth(child)
#             if childDepth > maxDepth:
#                 maxDepth = childDepth
#         return maxDepth + 1

def getDepth(node):
    if len(node['children']) == 0:
        return 0
    else:
        maxDepth = 0
        for child in node['children']:
            childDepth = getDepth(child)
            if childDepth > maxDepth:
                maxDepth = childDepth
        return maxDepth + 1


print(getDepth(root))

# inOrderTraverse(root)
# preOrderTraverse(root)
# postOrderTraverse(root)
