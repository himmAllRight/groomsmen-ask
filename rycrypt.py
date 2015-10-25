import random
from operator import itemgetter

def string2pairlist(s):
    pairList= []
    count = 0
    for c in s:
        pairList.append([count, c])
        count = count + 1
    random.shuffle(pairList)
    return(pairList)

    
def getIndFromPairlist(pl):
    return(",".join(map((lambda x: str(x[0])), pl)))

def getStringFromPairlist(pl):
    return("".join(map ((lambda x: x[1]), pl)))

def encrypt(s):
    pairList = string2pairlist(s)
    return(getIndFromPairlist(pairList), getStringFromPairlist(pairList))

def decrypt(pairList):
    indexList = pairList[0]
    s = pairList[1]
    m = list(map((lambda x, y: [x, y]), list(map(int, indexList.split(","))), s))
    m = sorted(m, key=itemgetter(0))
    return("".join(list(map((lambda x: x[1]), m))))

