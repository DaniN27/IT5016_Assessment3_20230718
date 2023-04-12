"""
ACTIVITY: PRACTISING USING FUNCTIONS WITH PARAMETERS

For each of your chosen challenges write at least 2 test case assertions in the form of comments at the end of each program.
Remember also to always use function parameters where needed!
Challenge 1
Write a program that prompts the user for their name and then their phone number (The program may store both as text) Use a function to output the following text:

Hello there, my name is < name of user > and my number is < phone number >.


"""

name = input("Please neter your first name:")
print("Thanks for your input")
number = input("Now enter your prefered contact number:")
if len(str(number)) > 10:
    print("That number is invalid, check your spelling and try again. ")
if len(str(number)) < 7:
    print("Your number is too short! Try again.")
else:
    print("Thanks for entering your number.")

def greet(name, number):
    print("Hello there, my name is", name," and my number is",number)

greet(name, number)

