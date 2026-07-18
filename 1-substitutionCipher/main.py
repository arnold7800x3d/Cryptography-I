from functions import ceasarCipher

print("""
    Welcome to the Ceasar Cipher. Use it to encrypt or decrypt your messages. Choose any function below.
    1. Encrypt a message
    2. Decrypt a message
    3. Exit    
""")
option = int(input("Enter the number matching your desired operation: "))

while(True):
    if option == 1:
        plaintext = input("Enter your message at the prompt: ")
        shiftValue = int(input("Choose a value between 0 - 25 for which to substitute your plaintext: "))

        if shiftValue > 25:
            shiftValue = int(input("The shift value is greater than 25! Choose a value between 0 - 25: "))

        ciphertext = ceasarCipher.ceasarEncryption(plaintext, shiftValue)
        print(ciphertext)
    elif option == 2:
        ciphertext = input("Enter your encrypted message at the prompt: ")
        shiftValue = int(input("Enter the shift value between 0 - 25 which was used for encryption: "))

        if shiftValue > 25:
            shiftValue = int(input("The shift value is greater than 25! Enter the key used for encryption: "))

        plaintext = ceasarCipher.ceasarDecryption(ciphertext, shiftValue)
        print(plaintext)
    else:
        print("Exiting...")
        exit
        break
    
