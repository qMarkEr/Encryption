string = "abсdef" #string(input())
key = "1 3 0 2" #string(input())  # space entry
def ByChar(string, key): 
    
    stringElems = [char for char in string] # separate by char
    
    keyElems = list(map(int, key.split(" ")))
    
    # if string > key then add zero chars
    for i in range (len(stringElems) % len(keyElems)):
        stringElems.append('\0')
    EncryptedString = [" "]*len(stringElems)
    shift = 0
    # if str > key then add \o and split string to blocks 
    for i in range (len(stringElems) // len(keyElems)):
        # encryption
        for index in range(len(keyElems)):
            EncryptedString[keyElems[index]+shift] = stringElems[index+shift]
        # shift indexes if str > key
        shift = shift + len(keyElems)
    #final string
    print("".join(EncryptedString))

ByChar(string, key)