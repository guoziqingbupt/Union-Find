from Quick_Find import *
from Quick_Union import *


def testForQuickFind(eleList, pairList):

    eleGroupNum = con_eleGroupNum(eleList)

    for elePair in pairList:
        quick_find(elePair, eleGroupNum)
    print(eleGroupNum)


def testForQuickUnion(eleList, pairList):

    eleNodeMap = genNodeList(eleList)

    for pair in pairList:
        quickUnion(pair, eleNodeMap)

    print([i.num for i in eleNodeMap.values()])


if __name__ == "__main__":
    eleList = [i for i in range(10)]
    pairList = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9), (5, 0)]
    testForQuickFind(eleList, pairList)
    testForQuickUnion(eleList, pairList)
