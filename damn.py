from KeyCheck import Check
from Encryption import Encrypting
from Decryption import Decrypting


# bool variable for entering data
enter = True


# exceptions
class RepeatException(Exception):
    pass
class GapException(Exception):
    pass
class InputException(Exception):
    pass
class EmptyException(Exception):
    pass

while(enter):
    print("What do you need: encrypt(e) or decrypt(d)?")
    global enc
    enc = str(input())
    if enc == "e":
        enter = False
        enc = "encrypt"
    elif enc == "d":
        enter = False
        enc = "decrypt"
    else:
        print("Wrong input. Try again")
    
        

print("Enter a message to %s: " %enc)
string = str(input())
enter = True
while(enter):

    stringElem = []
    print("Choose type of %sion: by words (w), by blocks (b), by cahracters (c): " %enc)
    x = input()
    match x:
        case "w":
            stringElem = string.split(" ")
            enter = False
        case "b":
            print("Enter the length of single block: ")
            step = int(input())
            enter = False
        case "c":
            stringElem = [elem for elem in string]
            enter = False
        case default:
            print("Wrong input! Try again")

    

enter = True

while (enter):


    print("Enter a key: ")
    key = str(input())  # space entry
    key = list(map(int, key.replace(" ", "")))
    keyElems = [elem for elem in key]
    Check(stringElem, keyElems)
    match Check(stringElem, keyElems):
        case 0:
            print("Input is empty. Try again")
        case 1:
            print("There is repeated element. Try again")
        case 2:
            print("Wrong input. It must start from 0. Try again")
        case 3:
            print("There is a gap in key. Try again")
        case 5:
            enter = False



        # if input correct break cycle and run encrypting function

match enc:
    case "encrypt":
        if x == "b":
            while len(string) % step != 0:
                string = string + "\0"
            for i in range (0, len(string), step):
                stringElem.append(string[i:i+step])
            Encrypting(stringElem, keyElems, x)
        else:
            Encrypting(stringElem, keyElems, x)
    case "decrypt":
        if x == "b":
            for i in range(0, len(string), step):
                stringElem.append(string[i:i + step])
            Decrypting(stringElem, keyElems, x)
        else:
            Decrypting(stringElem, keyElems, x)

    