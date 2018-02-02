# Encoding Magic Numbers: Integers
_work in progress..._

### Table Of Contents
* [Main Page](../README.md)
* Encoding Magic Numbers: Integers
* [link] XOR combination
* [link] XOR cipher
* [link] Detection
* [link] Encryption
* [link] Error-prone coding
* [link] AES-128 in ECB? *what?*
* [link] TBD
---
### Refreshing our minds with the number systems ( Magic Numbers )
N-bit encoding is a number system meant to represent numbers through a set of symbols or characters.  The N, in N-bit encoding, signifies the number of symbols and characters used to be the representation of a number.
```
For example: 
2-bit encoding system, otherwise known as Binary, which uses 1's and 0's.
16-bit encoding system, aka Hexadecimal, which uses the numbers 1 - 9 and the characters from A - F.
```
In our case to solve the first challenge, 64-bit ( otherwise known as Base64 ) encoding is used to encode binary data with 64 symbols and characters.  The characters usually being capitalized and lowercase letters from A-Z, while the symbols are + and /. 

Additionally, N-bit encoding is positionally set.  Meaning, that the position of the number within a given number, or the position of a symbol and/or character, matters for both encrypting and decrypting.
```
For example:
In a 2-bit binary system: 11100111 is always going to equal to 231, and 231 will always equal 11100111.
```
The reason behind the importance of the placement of the number lies in how we would go about encoding and decoding the given value.

### Encoding a number system

---
#### Bonus:
* [YouTube: schenken](https://www.youtube.com/watch?v=g8OhjcudKAo) - an excellent 4-min explanation on the basic concept behind Base64 Encoding