# Ask user if they want to generate a pasword or not
# If, yes ask for password length
# Generate password
# print the password
# if initial response is no then exit program
import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_pasword():
    password_length = int(input("How long would you like your password to be?"))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password? (Yes/No): ")

if option == "Yes":
    generate_pasword()
elif option == "No":
    print("Program ended")
    quit()
else:
    print("Invalid input, please input Yes or No")
    quit()