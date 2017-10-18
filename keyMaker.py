from generateKey import generateKey

class keyMaker():
    def makeKeys():
        keys_required = input("Keys needed (enter a number): ")
        x = keys_required
        keys_required = int(keys_required)
        while keys_required > 0:
            key = generateKey.generateKeyWhole()
            keys = open("keys.txt", "a")
            keys.write(key + "\n")
            keys.close()
            keys_required -= 1
        return (x + " keys generated - saved to file!")
