"""
    this file is used to represent the monoalphabetic ceaser cipher.
    it contains the encryption and decryption operations of the cipher
"""
import os
def ceasarEncryption(plaintext, shiftValue):
    ciphertext = ''
    for char in plaintext:
        # handle spaces within the message provided 
        if (ord(char)) == 32: 
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

def ceasarDecryption(ciphertext, shiftValue):
    plaintext = ''
    for char in ciphertext:
        # handle spaces within the ciphertext
        if(ord(char) == 32):
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

# def createTextFile():