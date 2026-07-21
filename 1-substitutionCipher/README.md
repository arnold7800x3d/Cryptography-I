# Substitution Cipher: Ceasar Cipher
Replace a letter of the alphabet with the letter standing (tradionally 3) places down the alphabet.  
Its monoalphabetic substitution can be summarized by the function:  
```
C = E(3,P) = (P+3) mod 26
```
> but the key is not only 3, so generally:
```
C = E(K,P) = (P+K) mod 26
```
> *where K is a value between 0 - 25*

## CLI Tool Implementation
This repository implements the Ceasar's Cipher in Python. It takes two approaches, which will each be discussed along with how to run the tool(s).

### Common Implementations Across Both Versions
For both versions, the common functionalities include:
- **Handling spaces and common punctuation marks**: These were simply added to the final output to ensure continuity and that the output message was still intelligible.
- **Saving the output to a file**: This is optional and allows instead of printing to the terminal, it saves the output to a file.
- **Reading the input from a file**: This allows taking the input message from a file if the message itself is too long to be typed in the terminal.

### ceasarCipherA.py
This initial approach uses the `ord()` and `chr()` Python functions.  
- `ord()`: This function takes a character and returns its corresponding unicode code.
```
ord("S") # prints 83
```
- `chr()`: This function operates as the reverse of `ord()`.
```
chr(83) # prints S
```
This first version of the tool captures the input message, loops over each character in the message and converts each character to its unicode value and adds the key before converting the final value to get the substituted equivalent of the initial character in the message.

### ceasarCipherB.py
This second approach makes use of a Python list, where the letters of the alphabet are initialized. It then loops over every character of the input message and matches each character to its position in the list by capturing its index. Once the index value is obtained, the index is added to the key and then the letter that sits at the index of the final value of this addition is the substituted equivalent of the initial character.
### Running the Tool(s)
This section discusses how to run the tool(s). Replace (x) in the commands with either A or B depending on which tool you want run.
On Windows, run:
```
python ceasarCipher(x).py -h
```
On Linux, run:
```
chmod u+x ceasarCipher(x).py
ceasarCipher(x).py
```
The output should look like this:
```
usage: ceasarCipher(x).py [-h] (-e | -d) (-m MESSAGE | -f FILE) [-k KEY] [-o]

Encrypt or decrypt messages using the Caesar Cipher, a classic substitution cipher that shifts each letter by a fixed number of positions.

options:
  -h, --help            show this help message and exit
  -e, --encrypt         encrypt the intended message (default: False)
  -d, --decrypt         decrypt the intended message (default: False)
  -m, --message MESSAGE
                        the message to process (wrap in quotes if it contains spaces)
  -f, --file FILE       file containing the message that needs to be processed (default: None)
  -k, --key KEY         number of positions to shift each letter (wraps around the alphabet, e.g. 3 shifts A - D) (default: 3)
  -o, --outputFile      save the result to output.txt in the current directory (instead of printing to the terminal) (default: False)

Built by: Arnold Ochieng'.
Developer GitHub link: https://github.com/arnold7800x3d
```
For basic encryption, run:
```
python ceasarCipher(x).py -e -m "HELLO WORLD" -k 10
```
Output:
```
ROVVY GYBVN
```
For decryption, use the -d flag.  
```
python ceasarCipher(x).py -d -m "ROVVY GYBVN" -k 10
```
Output:
```
HELLO WORLD
```
To save the output to a file:
```
python ceasarCipher(x).py -e/-d -m "message" -k number -o
```
Output:
```
Output saved in output.txt
```
Check for an `output.txt` file in the current working directory.
To get the input from a file, use a `.txt` file and run this command:
```
python ceasarCipher(x).py -e/-d -f input.txt -k number 
```
You can either print to the terminal or to a file.