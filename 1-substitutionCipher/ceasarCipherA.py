#!/usr/bin/env python3

"""
    this file is used to represent the monoalphabetic ceaser cipher.
    it contains the encryption and decryption operations of the cipher
"""
import os
import argparse

class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    pass

parser = argparse.ArgumentParser(
    formatter_class=CustomFormatter,
    description="Encrypt or decrypt messages using the Caesar Cipher, a classic substitution cipher " \
    "that shifts each letter by a fixed number of positions.",
    epilog="Built by: Arnold Ochieng'.\n"
           "Developer GitHub link: https://github.com/arnold7800x3d"
)

operationGroup = parser.add_mutually_exclusive_group(required=True)
operationGroup.add_argument(
    "-e", "--encrypt",
    action="store_true",
    help="encrypt the intended message"
)
operationGroup.add_argument(
    "-d", "--decrypt",
    action="store_true",
    help="decrypt the intended message"
)

parser.add_argument(
    "-m", "--message",
    type=str,
    required=True,
    help="the message to process (wrap in quotes if it contains spaces)"
)

parser.add_argument(
    "-k", "--key",
    type=int,
    default=3,
    help="number of positions to shift each letter (wraps around the alphabet, e.g. 3 shifts A - D)"
)

parser.add_argument(
    "-o", "--outputFile",
    action="store_true",
    help="save the result to output.txt in the current directory (instead of printing to the terminal)"
)

args = parser.parse_args()

def ceasarEncryption(plaintext, shiftValue=3):
    ciphertext = ''
    for char in plaintext:
        # handle spaces within the message provided 
        if ((ord(char)) == 32 or ord(char) == 44 or ord(char) == 46 or ord(char) == 39): 
            ciphertext += char
            continue # exit loop and go to the beginning

        char = char.upper() # convert to uppercase
        
        # handle the letter 'z'
        if (ord(char) == 90):
            temp = ord('A') + (shiftValue - 1)
        else:
            temp = ord(char) + shiftValue # substitute the letter at 'char' by the shift value
            # handle values whose ord() + the shift value = numbers which adding the (shift value - 1) will not yield a letter
            if (temp > 90):
                tempShiftValue = temp - ord('Z')
                temp = ord('A') + (tempShiftValue - 1)

        temp = chr(temp) # get the actual letter
        ciphertext += temp # store it in the final ciphertext

    return ciphertext

def ceasarDecryption(ciphertext, shiftValue=3):
    plaintext = ''
    for char in ciphertext:
        # handle spaces within the ciphertext
        if(ord(char) == 32 or ord(char) == 44 or ord(char) == 46 or ord(char) == 39):
            plaintext += char
            continue

        char = char.upper()

        # handle the letter 'a'
        if ord(char) == 65:
            temp = ord('Z') - (shiftValue - 1)
            # print(temp) 
        else:
            temp = ord(char) - shiftValue # substitute the letter at 'char' by the shitvalue
            # handle values whose ord(char) yield values less than 65 and thus will result in letters
            if (temp < 65):
                tempShiftValue = temp - ord('A')
                temp = ord('Z') + (tempShiftValue + 1)
        
        temp = chr(temp) # get the actual characters
        plaintext += temp
        
    return plaintext

# saving the output to a file
filePath = os.path.join(os.getcwd(), "output.txt")
def saveOutputToFile(originalMessage, resultMessage, isEncrypting):
    label1 = "Plaintext" if isEncrypting else "Ciphertext"
    label2 = "Ciphertext" if isEncrypting else "Plaintext"

    with open(filePath, 'w') as path:
        path.write(f"{label1}: {originalMessage} - {label2}: {resultMessage}")

    print("Output saved in output.txt")

if args.encrypt:
    output = ceasarEncryption(args.message, args.key)
else:
    output = ceasarDecryption(args.message, args.key)

if args.outputFile:
    saveOutputToFile(args.message, output, args.encrypt)
else:
    print(output)