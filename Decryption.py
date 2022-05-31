def Decrypting(string, keyElems, type):
    changed = False
    DecryptedString = []


    if len(string) <= len(keyElems):

        DecryptedString = [" "]*len(keyElems)
        RestoredStr = [" "]*len(keyElems)

        # restore string to encrypted one
        for i in range(len(DecryptedString)):
            if i < len(string):
                RestoredStr[i] = string[i]
            else:
                RestoredStr.insert(keyElems[i], "\0")
                changed = True

        # decryping...
        for i in range(len(DecryptedString)):
            DecryptedString[i] = RestoredStr[keyElems[i]]


    else:


        if len(string) % len(keyElems) == 0:

            DecryptedString = [" "]*len(string)
            shift = 0

            # decrypting...
            for i in range(len(string)):
                DecryptedString[i] = string[keyElems[i % len(keyElems)] + shift]
                if (i + 1) % len(keyElems) == 0:
                    shift = shift + len(keyElems)
        else:

            DecryptedString = [" "]*(len(string) + len(keyElems) - len(string) % len(keyElems))
            RestoredStr = [" "]*(len(string))
            shift = 0

            # restore string to encrypted one
            for i in range(len(DecryptedString)):
                if i < len(string):
                    RestoredStr[i] = string[i]
                else:
                    RestoredStr.insert(keyElems[i % len(keyElems)] + shift, "\0")
                    changed = True
                if (i+1) % len(keyElems) == 0:
                    shift = shift + len(keyElems)

            # decrypting...
            shift = 0
            for i in range(len(DecryptedString)):
                DecryptedString[i] = RestoredStr[keyElems[i % len(keyElems)] + shift]
                if (i + 1) % len(keyElems) == 0:
                    shift = shift + len(keyElems)

    if changed:
        while DecryptedString.count("\0") != 0:
            DecryptedString.remove('\0')

    # if the message was encrypted by words, join the items with a space
    if (type == "w"):
        print(" ".join(DecryptedString))
    else:
        print("".join(DecryptedString))
    
    

