class RepeatException(Exception):
    pass
class GapException(Exception):
    pass
class InputException(Exception):
    pass
class EmptyException(Exception):
    pass

def Check(string, keyElems):
    if len(keyElems) == 0:
        return 0

    for i in range(len(keyElems)):
        # if there was the same element before the current one: exception
        if keyElems[0:i].count(keyElems[i]) != 0:
            return 1

            
    # same key but sorted 
    tempKey = keyElems[:]
    tempKey.sort()

    # if user started input from 1
    if tempKey.count(0) == 0:
        return 2


    # if there is no some index: esception
    for i in range(1, len(tempKey)):
        if (tempKey[i-1] + 1) < tempKey[i]:
            return 3
    return 5
