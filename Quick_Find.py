

def con_eleGroupNum(eleList):
    """
    construct the element-group number map
    :param eleList: the list of distinct elements
    :return: the dictionary with the form {element: group number}
    """
    result = {}
    num = 1
    for i in eleList:
        result[i] = num
        num += 1
    return result


def change_GroupNum(pairGroupNum, eleGroupNum):
    """
    connect
    :param pairGroupNum: the two group numbers of the pair of elements
    :param eleGroupNum: the dictionary with the form {element: group number}
    :return: None
    """
    newGroupNum = min(pairGroupNum)
    for i in eleGroupNum:
        if eleGroupNum[i] == pairGroupNum[0] or eleGroupNum[i] == pairGroupNum[1]:
            eleGroupNum[i] = newGroupNum


def quick_find(elePair, eleGroupNum):
    """
    find and connect
    :param elePair: the pair of elements
    :param eleGroupNum: the dictionary
    :return: None
    """
    pairGroupNum = (eleGroupNum[elePair[0]], eleGroupNum[elePair[1]])
    change_GroupNum(pairGroupNum, eleGroupNum)
