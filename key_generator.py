from random import *
#generates 1/3 of the key
def generate_key_part():
    key_part = ""
    i = 0
    while i <= 4:
        coin = randint(0, 1)
        if coin == 0:
            #randomly generates letter using ASCII
            letter = randint(65, 90)
            letter = chr(letter)
            key_part += str(letter)
        else:
            #randomly generates a number 1-9 (not including 0)
            number = randint(1, 9) 
            number = str(number)
            key_part += number
        i += 1
    return(key_part)

#combines key parts to form full key
def generate_key_full():
    keys_required = input("Keys needed (enter a number): ")
    x = keys_required
    keys_required = int(keys_required)
    while keys_required > 0:
        key = ""
        j = 0
        while j <= 2:
            key += generate_key_part()
            key += "-"
            j += 1
        #cancerous fix to having an extra '-' at the end
        hotfix = list(key)
        del(hotfix[17])
        key = "".join(hotfix)

        keys = open("keys.txt", "a")
        keys.write(key+"\n")
        keys.close()
        keys_required -= 1
    return(x + "keys generated - saved to file!")
