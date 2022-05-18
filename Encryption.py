def Encrypting(string, keyElems): 
    ### string prepare

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

    ###

    shift = 0
    # if str > key then add \o and split string to blocks 
    for i in range (len(string) // len(keyElems)):

        # encryption
        for index in range(len(keyElems)):
            EncryptedString[keyElems[index]+shift] = string[index+shift]

        # shift indexes if str > key
        shift = shift + len(keyElems)

    #final string
    if changed:
        EncryptedString.remove('\0')

        
    print("".join(EncryptedString))