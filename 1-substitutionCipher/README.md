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
*where K is a value between 0 - 25*