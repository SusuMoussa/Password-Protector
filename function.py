import random

char = "qwertyuiopasdfghjklzxcvbnm"
char_len = len(char) - 1

capital_char = "QWERTYUIOPASDFGHJKLZXCVBNM"
capchar_len = len(capital_char) - 1

numbers = "1234567890"
numbers_len = len(numbers) - 1

symbols = "~!@#$%^&*()_+"
symbols_len = len(symbols) - 1

def passwordGenerator(length):
    password = ""

    for rep in range(0, int(length/4)):
        password = password + char[random.randint(0, char_len)]
        password = password + capital_char[random.randint(0, capchar_len)]
        password = password + numbers[random.randint(0,numbers_len)]
        password = password + symbols[random.randint(0, symbols_len)]

    while len ( password ) < length:
        index = random.randint(0, symbols_len)
        password = password + symbols[index]

    return password








# I will have 1 argument

# -----------------------------------------------------------------------------------------------------------------------

# define a function that takes a password as an argument and checks if it has a length lesser than 8 to print too short password
def safe(safepassword):
     f = open("text.txt", "w")
     f.write(safepassword)
     f.close()

def passwordchecker(passwordholder):
    if passwordholder < 8 :
        print ("This password is to short, anyone can acces your laptop ")

    else:
        print ("This password is a standard password, its better of this way.")
def analyzePassword(password):
        isChar = False
        isNumber = False
        isSymbol = False
        isCaptial = False
        if len(password) < 8:
            print("Your Password is Too Short")
        for character in char:
              if character in password:
                    isChar = True
        for character in symbols:
              if character in password:
                    isSymbol = True
        for character in numbers:
              if character in password:
                    isNumber = True
        for character in capital_char:
              if character in password:
                    isCaptial = True
        if isChar == False:
              print("There is no small characters in the password")
        if isCaptial == False:
              print("There is no capital characters in the password")
        if isSymbol == False:
              print("There is no Symbols in the password")
        if isNumber == False:
             print("there is no numbers in the password")