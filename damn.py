# bool variable for entering data
enter = True
# exceptions
class RepeatException(Exception):
    pass
class GapException(Exception):
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

def Encrypting(string, keyElems): 
    # \0 was added or not
    changed = False
    # if string length bigger then count of indexes then expand string to fit several keys
    if len(string) > len(keyElems):
        while(len(string) % len(keyElems)!= 0):
            string.append('\0')
        changed = True
    # add \0 if correct key have index more the length of string
    if len(string) < max(keyElems):
        for i in range (max(keyElems) - len(string)+1):
            string.append ('\0')
        changed = True
    EncryptedString = [" "]*len(string)
    
        
    shift = 0
    # if str > key then add \o and split string to blocks 
    for i in range (len(string) // len(keyElems)):
        # encryption
        for index in range(len(keyElems)):
            EncryptedString[keyElems[index]+shift] = string[index+shift]
        # shift indexes if str > key
        shift = shift + len(keyElems)
    #final string
   # if changed:
    #    EncryptedString.remove('\0')
    print("".join(EncryptedString))

while(enter):
    try:
        string = str(input())
        step = int(input())
        stringElem = []
        for i in range (0, len(string), step):
            stringElem.append(string[i:i+step])
        key = str(input())  # space entry
        keyElems = list(map(int, key.split(" ")))
        Check(stringElem, keyElems)
    except RepeatException: 
        print("There is repeted element in key. Try again")
    except GapException: 
        print("There is gap in key. Try again")
    else:
        # if input correct break cycle and run encryptikng function
        enter = False
        Encrypting(stringElem, keyElems)

    