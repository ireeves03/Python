#Phonetic Alphabet Dictionary
nato_alphabet = {
    "A": "Alpha", "a": "Alpha", "B": "Bravo", "b": "Bravo", "C": "Charlie", "c": "Charlie",
    "D": "Delta", "d": "Delta", "E": "Echo", "e": "Echo", "F": "Foxtrot", "f": "Foxtrot",
    "G": "Golf", "g": "Golf", "H": "Hotel", "h": "Hotel", "I": "India", "i": "India",
    "J": "Juliett", "j": "Juliett", "K": "Kilo", "k": "Kilo", "L": "Lima", "l": "Lima",
    "M": "Mike", "m": "Mike", "N": "November", "n": "November", "O": "Oscar", "o": "Oscar",
    "P": "Papa", "p": "Papa", "Q": "Quebec", "q": "Quebec", "R": "Romeo", "r": "Romeo",
    "S": "Sierra", "s": "Sierra", "T": "Tango", "t": "Tango", "U": "Uniform", "u": "Uniform",
    "V": "Victor", "v": "Victor", "W": "Whiskey", "w": "Whiskey", "X": "X-ray", "x": "X-ray",
    "Y": "Yankee", "y": "Yankee", "Z": "Zulu", "z": "Zulu"}

#Define the spelling function
def spell_word(word):
    for letter in word:
        if letter in nato_alphabet:
            print(nato_alphabet[letter])
#Define main function
def main():
    word = input("Enter a word: ")
    spell_word(word)
    
#calling function
main()