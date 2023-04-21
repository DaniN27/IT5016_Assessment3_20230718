#Write a program that takes user input string and converts it to Morse

def morse(text):
    code = {
         "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
        "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
        "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.", ".": ".-.-.-", ",": "--..--"
    }

    morse_text = ""

    for char in text.upper(): 
       if char in code: 
         morse_text += code[char] + ""

       else: 
             morse_text += char + " "
    
    morse_text = morse_text.strip()
    
    return morse_text

text = input("Enter text here to convert into Morse Code:")
print(morse(text))
