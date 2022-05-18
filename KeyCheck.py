class RepeatException(Exception):
    pass
class GapException(Exception):
    pass
class InputException(Exception):
    pass

def Check(string, keyElems):


    for i in range(len(keyElems)):
        # if there was the same element before the current one: esception
        if keyElems[0:i].count(keyElems[i]) != 0:
            raise RepeatException()

            
    # same key but sorted 
    tempKey = keyElems[:]
    tempKey.sort()

    # if user started input from 1
    if tempKey.count(0) == 0:
        raise GapException()


    # if there is no some index: esception
    for i in range(1, len(tempKey)):
        if (tempKey[i-1] + 1) < tempKey[i]:
            raise GapException()