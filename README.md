# Public_Key_Cryptosystem
Uploaded mainly python scripts of public key cryptosystem...
## RSA-OAEP.py: 
- remark:) These functions are for understanding RSA or RSA-OAEP easily, so do not strictly follow the RSA specification.
- 1st func: 3 variables(m: message, n: public key of RSA which the product 2 prime numbers, e: another public key) -> cipher text
- 2ed func: 3 variables(c: cipher text, d: secret key, n: public key) -> message
- 3rd func: hexadecimal -> CharacterCode (for example: 33 -> 3 and so on...)
- 4th func: it changes an integer array to a character string.
- 5th func: Refer to RSA specification or my OAEP.pdf for MGF(masked generation function). 
- 6th func: Refer to RSA specification or my OAEP.pdf for RSA-OAEP Encoding function.
- 7th func: Refer to RSA specification or my OAEP.pdf for RSA-OAEP Decoding function.
- remark:) I guess input r of RSA-OAEPDec is wrong, but it is for understanding RSA-OAEP.
