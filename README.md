# Public_Key_Cryptosystem
Uploaded mainly python scripts of public key cryptosystem...
## RSA-OAEP.py: 
- remark: These functions are for understanding RSA or RSA-OAEP easily, so do not strictly follow the RSA specification.
- 1st func: [RSA Encoding algorithm] 3 variables(_m_: message, _n_: public key of RSA which the product 2 prime numbers, _e_: another public key) -> cipher text
- 2ed func: [WRONG RSA Decoding algorithm] 3 variables(_c_: cipher text, _d_: secret key, _n_: public key) -> message
- 3rd func: hexadecimal -> CharacterCode (for example: 33 -> 3 and so on...)
- 4th func: it changes an integer array to a character string.
- 5th func: Refer to RSA specification or my document __OAEP.pdf__ for _MGF_(masked generation function). 
- 6th func: Refer to RSA specification or __OAEP.pdf__ for RSA-OAEP Encoding function.
- 7th func: Refer to RSA specification or __OAEP.pdf__ for RSA-OAEP Decoding function.
- remark: I guess the input _r_ of RSA-OAEPDec is wrong, but it is for understanding RSA-OAEP. I think input is not _r_ but _hLen_.

## paillier.py:
- remark: Refer to my document __paillier.tex__ which is written in Japanese(__jsarticle__), but if only you trace a stream of equations, you can understand paillier's theory.
- 1st func: LCM is the least common multiple.
- 2ed func: The key generation of Paillier Public Key Cryptosystem
- 3rd func: [Paillier Encoding algorithm] _r_ is a random integer except multiples of _p_ or _q_.
- 4th func: This function is useless, because the next function should contain it.
- 5th func: [Paillier Decoding algorithm] 
