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
string = input()
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
            for i in range (0, len(string), step):
                stringElem.append(string[i:i+step])
            
            enter = False
        case "c":
            stringElem = [elem for elem in string]
            enter = False
        case default:
            print("Wrong input! Try again")

    

enter = True

while (enter):

    try:    
        print("Enter a key: ")
        key = str(input())  # space entry
        key = list(map(int, key.replace(" ", "")))
        keyElems = [elem for elem in key]
        Check(stringElem, keyElems)
    
    except RepeatException: 
        print("There is repeted element in key. Try again")

    except GapException: 
        print("There is gap in key. Try again")

    else:
        # if input correct break cycle and run encryptikng function
        enter = False
        match enc:
            case "encrypt":
                
                Encrypting(stringElem, keyElems)
            case "decrypt":
                Decrypting(stringElem, keyElems)

    