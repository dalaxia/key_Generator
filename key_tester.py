def key_redemption(i):
    keys = open("keys.txt", "r+")
    redeemed_key = keys.readline(i)
    keys.
              
def key_test(i):
    i = 0
    key = input("Please enter your key: ")
    keys = open("keys.txt", "r")
    total_keys = sum(1 for _ in keys)
    keys.close()
    keys = open("keys.txt", "r")
    print("Searching for... '" + key + "'")
    #test keys max
    while i <= total_keys:
        test_key = keys.readline()
        test_key = test_key.rstrip("\n")
        if test_key == key:
            total_keys = str(total_keys)
            key_redemption(i)
            print("After searching through " + total_keys + " keys...")
            return("We found your key - enjoy!")
        else:
            i += 1
            
    #unable to find key        
    if i >= total_keys:
        total_keys = str(total_keys)
        print("After searching through " + total_keys + " keys...")
    return("We were unable to find your key - sorry!")
    
