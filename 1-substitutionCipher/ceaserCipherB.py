"""
    this is the second version of the implementation of the ceaser cipher.
    it takes a different approach by using arrays. 
"""
import argparse
import os

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description="Encrypt or decrypt messages using the Caesar Cipher, a classic substitution cipher " \
    "that shifts each letter by a fixed number of positions.",
    epilog="Built by arnold7800x3d"
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

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# encryption function
def ceaserEncryption(plaintext, shiftValue=3):
    ciphertext = ''
    for char in plaintext:
        if char == ' ':
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
        if char == ' ':
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
filePath = os.path.join(os.getcwd(), "output.txt")
def saveOutputToFile(originalMessage, resultMessage, isEncrypting):
    label1 = "Plaintext" if isEncrypting else "Ciphertext"
    label2 = "Ciphertext" if isEncrypting else "Plaintext"

    with open(filePath, 'w') as path:
        path.write(f"{label1}: {originalMessage} - {label2}: {resultMessage}")

    print("Output saved in output.txt")

if args.encrypt:
    output = ceaserEncryption(args.message, args.key)
else:
    output = ceasarDecryption(args.message, args.key)

if args.outputFile:
    saveOutputToFile(args.message, output, args.encrypt)
else:
    print(output)

