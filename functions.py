"""
print('')
float()
int()
str()
input()
Are all also commonly used Python functions

"""


def my_function():
    print ("Welcome to my functions program!")
my_function()
print("")

def greet(name):
    print("Hi", name)
    print("How are you?")
greet("Dani")
print("")


def add_numbers(num1, num2):
    result = num1 + num2
    print ("This equals", result)

num1 = 5
num2 = 7

add_numbers(num1, num2)

print("")

def sub_numbers(num3, num4):
    equals = num3 - num4
    return equals

num3 = 2548
num4 = 1483

equals = sub_numbers(num3, num4)
print("The sum is", equals)
print("")
print("")
#Using length function for a list

print("36, 78, 26, 45, 12, 20")
numbers = [36, 78, 26, 45, 12, 20]

length = len(numbers)
print("The length of our list is", length)

#We can also use the sum function to find the combined total of our numbers listed

numbers_sum = sum(numbers)
print("The combined total is", numbers_sum)

#Getting full name function


def full_name (first, last):
    full_name = first + " " + last
    return full_name

first = "Dani" 
last = "Gordon"
name = full_name (first, last)
print ("Hello, how are you", name)   
print("")

