def Encrypting(string, keyElems, type): 
    ### string prepare

    # \0 was added or not
    changed = False

    # if string length is greater than count of indexes then expand string to fit several keys
    if len(string) > len(keyElems):
        while(len(string) % len(keyElems)!= 0):
            string.append('\0')
            changed = True


    # add \0 if correct key have index more the length of string
    if len(string) <= max(keyElems):
        for i in range (max(keyElems) - len(string)+1):
            string.append ('\0')
            changed = True

    EncryptedString = [" "]*len(string)

    ###

    shift = 0
    
    # encrypting...
    if  len(keyElems) == len(string):
        for i in range(len(string)):
            EncryptedString[keyElems[i]] = string[i] 
    else:
        for i in range(len(string)):
            EncryptedString[keyElems[i % len(keyElems)] + shift] = string[i]

            if (i+1) % len(keyElems) == 0:
                shift = shift + len(keyElems)

    # final string
    if changed:
        while EncryptedString.count("\0") != 0:
            EncryptedString.remove('\0')
    
    if type == "w":
        print(" ".join(EncryptedString))
    else:
        print("".join(EncryptedString))
