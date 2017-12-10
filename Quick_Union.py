class UFTreeNode(object):
    def __init__(self, num):
        # the group number
        self.num = num

        # its children
        self.children = []

        # its parent
        self.parent = None

        # the number of nodes that rooted by this node
        self.weight = 1


def genNodeList(eleList):
    """
    generating the node of each element
    :param eleList: the list of elements
    :return: a dictionary formed as {element: corresponding node}
    """
    result = {}
    for ele in eleList:
        result[ele] = UFTreeNode(ele)
    return result


def locPair(elePair, eleNodeMap):
    """
    locate the positions of the pair of elements
    :param elePair:
    :param eleNodeMap: a dictionary formed as {element: corresponding node}
    :return: the two nodes of the pair of elements
    """

    return [eleNodeMap[elePair[0]], eleNodeMap[elePair[1]]]


def backtracking(node):
    """
    1. find the root of a node
    2. cut down the height of the tree
    :param node:
    :return: the root of node
    """
    root = node

    while root.parent:
        cur = root
        root = root.parent

        # the grandfather node of cur exists
        if cur.parent.parent:

            # make the father of cur is its grandfather
            grandfather = cur.parent.parent
            grandfather.children.append(cur)

    return root


def quickUnion(elePair, eleNodeMap):
    """
    union process
    :param elePair:
    :param eleNodeMap:
    :return:
    """
    nodePair = locPair(elePair, eleNodeMap)

    root_1, root_2 = backtracking(nodePair[0]), backtracking(nodePair[1])

    # if the two elements of the pair are not belongs to the same root (group)
    if root_1 is not root_2:

        if root_1.weight >= root_2.weight:

            # update weight
            root_1.weight += root_2.weight

            # make the root2 as a subtree of root1
            root_1.children.append(root_2)

            # update the group number of root2
            root_2.num = root_1.num

        else:
            root_2.weight += root_1.weight
            root_2.children.append(root_1)
            root_1.num = root_2.num