# -*- coding: utf-8 -*-
import random
from Crypto.Util.number import *


# L.C.M
def LCM(p, q):
    return p / GCD(p, q) * q


# Paillier Key Generator
def PailKeyGen(p, q):
    flag = 0
    if GCD(p * q, (p - 1) * (q - 1)) != 1:
        return False
    else:
        n = p * q
        n2 = n ** 2
        lam = LCM(p - 1, q - 1)
        while flag != 1:
            alpha = random.randint(1, n2 - 1)
            beta = random.randint(1, n2 - 1)
            if alpha % p == 0 or alpha % q == 0:
                continue
            elif beta % p == 0 or beta % q == 0:
                continue
            else:
                flag = 1
        g = ((1 + alpha * n) * pow(beta, n, n2)) % n2
        return [n, g, lam]


# Paillier Encoding
def PailEnc(m, n, g):
    flag = 0
    n2 = n * n
    while flag != 1:
        r = random.randint(1, n2 - 1)
        if r % n == 0 or r % 2 != 0:
            continue
        else:
            flag = 1
    return (pow(g, m, n2) * pow(r, n, n2)) % n2


# Pailier L function
def L(x, n):
    return (x - 1) / n


# Paillier Decoding
def PailDec(c, lam, n, g):
    n2 = n ** 2
    return (L(pow(c, lam, n2), n) * inverse(L(pow(g, lam, n2), n), n2)) % n


if __name__ == '__main__':
    # test data
    m = 19910813
    p = 11680610569588790846719050387635150916386537519628391505052616220025069169334914985978494552300113597095435612762082695306304849762531442299009542540057807
    q = 11635960520674358921712306047987978111551452881537167964799128382131248473653748336593826937633397637078845204883116714935776408687981753746402668472432183
    key = PailKeyGen(p, q)
    n = key[0]
    g = key[1]
    lam = key[2]
    c = PailEnc(m, n, g)
    print PailDec(c, lam, n, g)
