# A program to implement vigenere's cipher.
# It take the keyword as an cmd line arg and plaintext from user
# and process it to print a scrambled version of plain text.

from sys import argv
from cs50 import get_string

def main():
    # check number of arguments
    if len(argv) != 2:
        print("Usage: python vigenere.py keyword")
        exit(1)
    
    # check whether each character is alphabet or not
    if not argv[1].isalpha():
        print("Usage: python vigenere.py keyword")
        exit(2)
    
    # input plaintext
    text = get_string("plaintext: ")

    # vigenere's cipher -->
    j = 0   # represents keywords letter
    ctext = [ch for ch in text]
    for i in range(len(text)):
        if argv[1][j].isupper():
            key = (ord(argv[1][j])) % (ord('A')) # find the key as A = a = 0... ord gives ascii value of alphabet
        elif argv[1][j].islower():
            key = (ord(argv[1][j])) % (ord('a'))
        
        if text[i].isupper():
            shift = ord(text[i]) + key
            while shift > ord('Z'): # wrapping from above 'Z'
                shift = (ord('A') - 1) + (shift % ord('Z'))
            ctext[i] = chr(shift)

            if(j < len(argv[1]) - 1):
                j += 1
            else:
                j = 0
        elif text[i].islower():
            shift = ord(text[i]) + key
            while shift > ord('z'): # wrapping from above 'Z'
                shift = (ord('a') - 1) + (shift % ord('z'))
            ctext[i] = chr(shift)

            if(j < len(argv[1]) - 1):
                j += 1
            else:
                j = 0

    # printing ciphertext
    print("ciphertext:", end=" ")
    for i in range(len(ctext)):
        print(ctext[i], end="")
    print()

if __name__ == "__main__":
    main()