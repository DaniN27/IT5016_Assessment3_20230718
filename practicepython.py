"""
ACTIVITY: PRACTISING USING FUNCTIONS WITH PARAMETERS
Read through all of the following challenges.
Choose any 3 and then write a Python program for each one.
For each of your chosen challenges write at least 2 test case assertions in the form of comments at the end of each program.
Remember also to always use function parameters where needed!
Challenge 1
Write a program that prompts the user for their name and then their phone number (The program may store both as text) Use a function to output the following text:

Hello there, my name is < name of user > and my number is < phone number >.

Challenge 2
Write a program that prompts the user for a number and then outputs the first 4 multiples of that number. You must use a loop in your method. Assume that the user enters a valid positive integer.

Challenge 3
Write a program that prompts the user to enter the integers x and y. The program must then output the first y multiples of x separated by commas. An example is:
x = 4 and y = 3  output = 4, 8, 12.

Challenge 4
Write a function that sums all the numbers in a stored list.

Challenge 5
Write a function that calculates and displays the number of upper and lowercase letters in a stored string.

Challenge 6
Write a Python program to print the even numbers from a stored list.
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

