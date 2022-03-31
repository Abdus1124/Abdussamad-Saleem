def enc():  # function to encrypt
    string, s=input("Enter the string to be encoded: "), int(input("Enter the shift value: "))
    outcome = ""
    for i in range(len(string)):
        characters = string[i]
        if (characters.islower()):
            outcome += chr((ord(characters) + s - 97) % 26 + 97)
        else:
            outcome += characters        
    print("Encrypted string: ",outcome)
#Function to decrypt            
def dec():
    message, s = input("Enter the string to be decoded: "), input("Enter the word from plainstring: ")

    LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    
    for key in range(len(LETTERS)):   
            translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:


                translated = translated + symbol
        if s in translated:
            
            break
    print('The encryption key is: %s\n Plainstring: %s' % (key, translated))
while(True):
    ch=input("\nEnter \n'e' to encrypt\n'd' to decrypt\n'q' to quit:\n")
    if ch=='e' :
        enc()
    elif ch=='d':
        dec()
    elif ch=='q':
        break
    else:
        print("Wrong input! Try again: ")