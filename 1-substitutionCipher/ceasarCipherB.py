#!/usr/bin/env python3

"""
    this is the second version of the implementation of the ceaser cipher.
    it takes a different approach by using arrays. 
"""

import argparse
import os

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

inputSource = parser.add_mutually_exclusive_group(required=True)
inputSource.add_argument(
    "-m", "--message",
    type=str,
    help="the message to process (wrap in quotes if it contains spaces)"
)
inputSource.add_argument(
    "-f", "--file",
    type=str,
    help="file containing the message that needs to be processed"
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

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# encryption function
def ceasarEncryption(plaintext, shiftValue=3):
    ciphertext = ''
    for char in plaintext:
        if (char == ' ' or char == '.' or char == ',' or char == '\''):
            ciphertext += char
            continue

        char = char.upper()
        if char in letters:
            charIndex = letters.index(char)

            # handle letter 'z'
            if charIndex == 25:
                cipherIndex = letters.index('A') + (shiftValue - 1)
            else:
                cipherIndex = charIndex + shiftValue # get the index of the cipher 'letter' from the letters array
                if cipherIndex > 25: # handle situations where the cipherIndex is out of range (past 25)
                    tempCipherIndex = cipherIndex - letters.index('Z')
                    cipherIndex = letters.index('A') + (tempCipherIndex - 1)

            temp = letters[cipherIndex]
            
        ciphertext += temp
    
    return ciphertext

# decryption function
def ceasarDecryption(ciphertext, shiftValue=3):
    plaintext = ''
    for char in ciphertext:
        if (char == ' ' or char == '.' or char == ',' or char == '\''):
            plaintext += char
            continue

        char = char.upper()

        if char in letters:
            charIndex = letters.index(char)

            # handle letter 'a'
            if charIndex == 0:
                plainIndex = letters.index('Z') - (shiftValue - 1)
            else:
                plainIndex = charIndex - shiftValue
                if plainIndex < 0:
                    plainIndex = letters.index('Z') + (plainIndex + 1)

            temp = letters[plainIndex]
            plaintext += temp 
    
    return plaintext

# saving the output to a file
outputFilePath = os.path.join(os.getcwd(), "output.txt")
def saveOutputToFile(originalMessage, resultMessage, isEncrypting):
    label1 = "Plaintext" if isEncrypting else "Ciphertext"
    label2 = "Ciphertext" if isEncrypting else "Plaintext"

    with open(outputFilePath, 'w') as path:
        path.write(f"{label1}: {originalMessage}\n{label2}: {resultMessage}")

    print("Output saved in output.txt")

# reading text from a file
def readInputFromFile(inputFilePath):
    with open(inputFilePath, 'r') as path:
        originalMessage = path.read()

    return originalMessage

if args.file is None:
    messageContent = args.message
else:
    messageContent = readInputFromFile(args.file)

if args.encrypt:
    output = ceasarEncryption(messageContent, args.key)
else:
    output = ceasarDecryption(messageContent, args.key)

if args.outputFile:
    saveOutputToFile(messageContent, output, args.encrypt)
else:
    print(output)