import function


steps = [
    "Never Use The Same Password Everywhere",
    "Have a Personal Password That's Never Shared Before",
    "Have a One or Multiple Passwords, That you can share with your family/friends",
    "Never Store Your Passwords in a file on your computer, instead on a physcial paper",
    "Never use or rely on a Weak password",
    "Never trust any link that asks for your credientials, it might be phishing",
]




print("============ Personal password factory ============ ")

for step in steps:
    print("->", step)

print("Generated Password is: ", function.passwordGenerator(4))

function.analyzePassword("SusuLoves***1")

c = function.passwordGenerator(10)

function.safe(c)
function.analyzePassword(c)

menu = """
    1-) Generate a password
    2-) analyze a password
    3-) store a password in a file called text.txt
    4-) exit
"""

print (menu)

while True:
    choice = input("choose:")
    if choice == "4":
        exit()

    if choice == "1":
        length = int(input("enter password length: "))
        generated = function.passwordGenerator(length)
        print ("generated password ", generated)
    elif choice == "2":
        toanalayze = input("password to analyze: ")
        function.analyzePassword(toanalayze)
    elif choice == "3":
        tostore = input("password to store: ")
        function.store(tostore)
    else:
        print("Option not found")