from random import *
class generateKey():
    def generateKeyPart():
        keyPart = []
        x = 0
        while x <= 4:
            #choice between letter and number
            char = randint(0, 1)
            if char == 0:
                letter = randint(65, 90)
                #convert to character
                letter = chr(letter)
                #convert to string
                letter = str(letter)
                keyPart.append(letter)
                x += 1
            else:
                number = randint(1, 9)
                #convert to string
                number = str(number)
                keyPart.append(number)
                x += 1
        keyP = ''.join(keyPart)
        return(keyP)

    def generateKeyWhole():
        from generateKey import generateKey
        key = ""
        x = 0
        while x <= 4:
            key += generateKey.generateKeyPart()
            key += "-"
            x += 1
        hotfix = list(key)
        del(hotfix[29])
        key = ''.join(hotfix)
        return(key)
