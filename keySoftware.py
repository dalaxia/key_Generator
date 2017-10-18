from generateKey import generateKey
from keyMaker import keyMaker

class keyInitiate():
    answer = input("What would you like to do? [G]enerate, [E]rase or [R]edeem keys.\n")
    if(answer == "G"):
        print(keyMaker.makeKeys())
    elif(answer == "E"):
        open("keys.txt", "w").close()
        print("Keys erased!")
    #elif(answer =="R"):
        #redemption WIP
