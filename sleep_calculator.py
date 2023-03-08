# UserEntry.py
# author: D. G.
# Sleep calculator (avg. 7 hours) (2555 a year)

print ("Welcome to sleep calculator\n")
user_yob = int(input("Please enter your year of birth\n"))
age=2023-user_yob
print ("Thanks for your input\n")
print ("The year of birth you have entered is ", user_yob)
print ("If your average sleep is 7 hours a night then\n")
print('You have approximately slept', 2555 * age, " hours in your lifetime\n")
