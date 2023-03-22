"""
Create a calculator to gather input from a user.

Specifications:

-Taxable earnings in a year must be more than $500 and less than $2,000,000.00
-User must be able to enter text non-formatable
-Final calculation must displayed with $ symbol
-Operation must only show input and the output
-Doesn't need to inclue; detailed explanation of workings or % taxed just the final total

"""
print("Use this calculator to find out how much you were taxed within the last ammun")
print("")
income = int(input("Please enter your income in the format ##### (no spaces or $) here: "))

if income < 500:
    print("Error, this in an invalid number for this equation.")

elif income > 1000000000:
    print("Sorry, this number is too high. Be realistic. ")

elif income <= 14000: 
    tax = income * (10.5/100) 
    print(f"You were taxed {tax} in the last tax year")

elif income> 14000 and income <= 48000:
    tax = (income - 14000) * (17.5/100) + 1470
    print(f"You were taxed {tax} in the last tax year")

elif income> 48000 and income <= 70000:
    tax = (income - 48000) * (30/100) + 7420
    print(f"You were taxed {tax} in the last tax year")

elif income > 70000 and income <= 180000:
    tax = income * (33/100) + 14020
    print(f"You were taxed {tax} in the last tax year")
    
elif income >= 180001:
    tax = income * (39/100) + 50320
    print(f"You were taxed {tax} in the last tax year")


