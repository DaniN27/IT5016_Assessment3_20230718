"""
Chinese Zodiac cycle runs every 12 years, then in repeats
Make a calculator to assign a animal to the year input
2000 Dragon
2001 Snake
2002 Horse
2003 Sheep
2004 Monkey
2005 Rooster
2006 Dog
2007 Pig
2008 Rat
2009 Ox
2010 Tiger
2011 Hare
"""

from time import sleep

print("")
print("")
print("Want know your assigned Chinese Zodiac animal?")
print ("")
print("Find out now!")
print("")

user_yob = int(input("Enter the year you were born in here:"))

if (user_yob - 2000) % 12 == 0:
     sign = 'Dragon' 

elif (user_yob - 2000) % 12 == 1:
     sign = 'Snake'

elif (user_yob - 2000) % 12 == 2:   
    sign = 'Horse'

elif (user_yob - 2000) % 12 == 3:
    sign = 'Sheep'

elif (user_yob - 2000) % 12 == 4:
    sign = 'Monkey'  

elif (user_yob - 2000) % 12 == 5:
    sign = 'Rooster'  

elif (user_yob - 2000) % 12 == 6:   
    sign = 'Dog'

elif (user_yob - 2000) % 12 == 7:
    sign = 'Pig'

elif (user_yob - 2000) % 12 == 8:
    sign = 'Rat'

elif (user_yob - 2000) % 12 == 9:
    sign = 'Ox'  

elif (user_yob - 2000) % 12 == 10:
    sign = 'Tiger'   

elif (user_yob - 2000) % 12 == 11:
    sign = 'Hare'


print("")
print("Thanks for your input.")
print("")
print(f'You have enterted:{user_yob}')
print("")
print("")
print("Loading..")
sleep(2)
print("")
print("")
print("Loading...")
sleep(1)
print("")
print("")
print("Loading....")
sleep(3)
print("")
print("")
print("Loading.....")
sleep(1)
print("")
print("")
print("Loading......")
sleep(4)
print("")

print("Your Chinese Zodiac animal is:", sign)

print("")

print("Want to learn more about your Zodiac?")

print("")

zodiac = str(input("Enter your Chinese Zodiac animal here:"))

print ("")

print(f'You have entered "{zodiac}", seemingly born under a lucky star, the {zodiac} is the most vital and powerful of any in the Chinese zodiac, although with an infamous reputation for being hotheaded - and possessing a sharp tongue!')

print("Thanks for using this Zodiac calculator, try our sleep calculator next!")

print("")