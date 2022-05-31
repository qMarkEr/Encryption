from KeyCheck import Check
from Encryption import Encrypting
from Decryption import Decrypting


# bool variable for entering data
enter = True

while(enter):
    print("What do you need: encrypt(e) or decrypt(d)?")
    global enc
    enc = str(input())
    if enc == "e":
        enc = "encrypt"
        enter = False
    elif enc == "d":
        enc = "decrypt"
        enter = False
    else:
        print("Wrong input. Try again")
    
        

print("Enter a message to %s: " %enc)
string = str(input())
enter = True
while(enter):

    stringElem = []
    print("Choose type of %sion: by words (w), by blocks (b), by cahracters (c): " %enc)
    type = input()
    match type:
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
        case 4:
            enter = False


# if input correct break cycle and run encrypting function

match enc:
    case "encrypt":

        # specific split to blocks
        if type == "b":
            string = string + "\0"*(step - len(string) % step)
            for i in range(0, len(string), step):
                stringElem.append(string[i:i+step])
            Encrypting(stringElem, keyElems, type)
        else:
            Encrypting(stringElem, keyElems, type)
    case "decrypt":

        # split to blocks
        if type == "b":
            for i in range(0, len(string), step):
                stringElem.append(string[i:i + step])
            Decrypting(stringElem, keyElems, type)
        else:
            Decrypting(stringElem, keyElems, type)

    