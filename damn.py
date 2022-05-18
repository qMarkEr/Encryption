from KeyCheck import Check
from Encryption import Encrypting



# bool variable for entering data
enter = True


# exceptions
class RepeatException(Exception):
    pass
class GapException(Exception):
    pass
class InputException(Exception):
    pass



print("Enter a message to encrypt: ")
string = str(input())

while(enter):
    try:
        stringElem = []
        print("Choose type of encryption: by words (w), by blocks (b), by cahracters (c): ")
        x = str(input())
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
                raise InputException()


    except InputException:
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
        Encrypting(stringElem, keyElems)

    