# Comaprison operators:
"""
<       Less than
>       Greater than
==      Equal
!=      Not equal to
>=      Greater than or equal to
<=      Less than or equal to
"""
number = 15
print (number > 10)

#True boolean value

# Logical Operators :
'''
and     True if both operands are True
or      True if either of the operands is True
not     True if operand is False

'''

age = 22
gpa = 3.8
result = age >= 18 and  gpa > 3.6
print(result)
# In this scenario our variables (age, gpa) must both be greater than 18 and 3.6 to be true, if one is wrong it will be false.
# Using the [or] operator either or need to be higher for this expression to be true.
# The [not] operator negates any result that is correct or wrong to it's opposing counterpart.

# Decision making
'''
Below I will demonstrate an if statement for a test score, to show if someone passed

'''
results = int(input("Enter your results here:"))

if results >= 50:
    print("Congratulations you have passed!")

if results < 50:
    print("You have not passed at this time")   
    print("Better luck next time!")
# In this example we have preformed a simple if statement for acheieving higher than 50 on a test score

# if/else statements
score = 35

if score >= 50:
    print("You have passed, well done!")

else:
    print("Unfortunately, you have not passed at this time")

#elif statements

score = 105

if score > 100 or score < 0:
    print("You have enterted invalid input")

elif score >= 50:
    print("Congrats! You passed")
else:
    print("You failed, try harder next time")

#python 1.1.1.8

#while loop 

count = 0

while count < 5:
    print("I am in a loop")
    print("This is a cool loop feature of Python")
    count = count + 1
#This is a while loop, while the test condition is true (Less than 5) the loop will run again and again.
#We can control how many times we run this loop by increasing count by 1, as long as the test condition is true our print text will run.
#Adding in the count = count + 1 will raise the value of count(0) by 1 untill we get to 5 and our while condition is no longer true.

count = 1

while count < 6:
    print(count)
    count = count +1
    

#For loop
text = 'Python'

for character in text:
    print(character)
    