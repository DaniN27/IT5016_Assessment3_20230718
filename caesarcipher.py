"""
Alpahet cipher program 
Needs to take a number input from user, more than 1 and no limit
Needs to display end result back to user
Should use loops
"""
def caesar_cipher(text,shift):
    result=""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result +=chr((ord(char) + shift - 65) % 26 + 65)

            else:
               result += chr((ord(char) + shift - 97) % 26 + 97)

    else:
                 result += char

    return result

print(" To use this cipher first we must enter a value to rotate our alphabet and a short word or phrase ")
print("")

cipher = (input("To begin first enter a phrase or word to encrypt:"))

number = int(input("Enter any number above 1 to begin: "))

if number < 1: 
    print("Sorry this number is too low, try again.")

else:
    encrypted_text = caesar_cipher(cipher, number)
    print("The encrypted text is:", encrypted_text)



"""
g = ord ('A')
65 + def = 68

h = chr (68)
D
/
"""



