import random
import string

charecters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
def PassGen():
    Size = input("Enter Password Length (MAX = 100): ")
    Size = int(Size)

    password = random.sample(charecters, Size)

    password = "".join(password)
    print(password)
    yorn = input("Do you want another password?(y/n): ")
    if yorn == "y":
        PassGen()
    if yorn == "Y":
        PassGen()
    if yorn == "n":
        "Alright, Have a nice day!"
        quit()
    if yorn == "N":
        "Alright, Have a nice day!"
        quit()
    else:
        print("Invalid Syntax, Closing Program...")
        quit()

PassGen()