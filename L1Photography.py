# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    idxDic = {}
    for i in range(N):
        if C[i] in idxDic.keys():
            idxDic[C[i]] = idxDic[C[i]] + [i]
        else:
            idxDic[C[i]] = [i]

    if len(idxDic.keys()) < 3: return 0

    res = 0
    for i in idxDic['P']:
        for j in idxDic['students']:
            for k in idxDic['sandwiches']:
                if X <= (j - i) <= Y and X <= (k - j) <= Y:
                    res = res + 1
                if X <= (j - k) <= Y and X <= (i - j) <= Y:
                    res = res + 1

    return res


def getArtisticPhotographCount2(N: int, C: str, X: int, Y: int) -> int:
    idxDic = {}
    for i in range(N):
        if C[i] in idxDic.keys():
            idxDic[C[i]] = idxDic[C[i]] + [i]
        else:
            idxDic[C[i]] = [i]

    if len(idxDic.keys()) < 3: return 0

    res = 0
    for i in idxDic['P']:
        idxJ = findIdx(i, idxDic['students'])
        for j in idxDic['students'][idxJ:]:
            idxK = findIdx(j, idxDic['sandwiches'])
            for k in idxDic['sandwiches'][idxK:]:
                if X <= (j - i) <= Y and X <= (k - j) <= Y:
                    res = res + 1

    for i in idxDic['sandwiches']:
        idxJ = findIdx(i, idxDic['students'])
        for j in idxDic['students'][idxJ:]:
            idxK = findIdx(j, idxDic['P'])
            for k in idxDic['P'][idxK:]:
                if X <= (j - i) <= Y and X <= (k - j) <= Y:
                    res = res + 1

    return res

def findIdx(target, rangeSorted):
    res = 0

    for i, val in enumerate(rangeSorted):
        if val >= target:
            return i

    return res


print(getArtisticPhotographCount(N=5, C='APABA', X=1, Y=2))
print(getArtisticPhotographCount(N=5, C='APABA', X=2, Y=3))
print(getArtisticPhotographCount(N=8, C='.PBAAP.sandwiches', X=1, Y=3))
