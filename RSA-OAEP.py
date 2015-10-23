# -*- coding: utf-8 -*-
#
# This source is about RSA-OAEP.
# Please check your python installing pycrypto.
# Please read my document: RSA-OAEP.pdf because I explained functions and variables.
# This source can move on python2.7.10 
# H27(2015)-10-23. Writen by Akihiko GONDA.
#
import math
import random
import hashlib
from Crypto.Util.number import *

def RSAEnc(m, n, e):
    return pow(m, e, n)    

def RSADec(c, d, n):
    return pow(c, d, n)

def HexstringToCharacters(hexstr):
    clen = len(hexstr)
    if clen & 1 == 1:
        hexdata = hexstr[0]
        outdata = chr(int(hexdata, 16))
        c = 1
    else:
        outdata = "" 
        c = 0
    for i in range(c, clen, 2):
        hexdata = hexstr[i : i + 2]
        outdata = outdata + chr(int(hexdata, 16))
    return outdata

def FrmoCharacterToCode(arr):
    outdata = ""
    for i in range(len(arr)):
        outdata = outdata + chr(arr[i])
    return outdata

def MGF(seed, dLen):
    dchar = HexstringToCharacters(seed)
    c1 = int(math.floor(dLen * 1.0 / 20))
    indata = dchar + FrmoCharacterToCode([0, 0, 0, 0])
    outdata = int(hashlib.sha1(indata).hexdigest(), 16)
    for i in range(1, c1 + 1):
        indata = dchar + FrmoCharacterToCode([0, 0, 0, i])
        outdata = outdata * pow(2, 160) + int(hashlib.sha1(indata).hexdigest(), 16)
    outdata = outdata >> int((c1 + 1) * 160 - dLen * 8)
    return hex(outdata)[2 : int(2 * dLen + 2)]

def RSAOAEPEnc(m, mLen, n, e, r):
    if mLen != len(m) / 2:
        return False
    k = int(math.ceil(size(n) / 8))
    k2 = mLen
    k0 = int(math.ceil(size(r) / 8))
    k1 = k - 2 * k0 - k2 - 2
    if k1 < 0:
        return False
    lhash = hashlib.sha1().hexdigest()
    hLen = len(lhash) / 2
    x01 = "01"
    x00 = "00"
    ps = []
    while len(ps) != 2 * k1:
        ps.append("0")
    ps = "".join(ps)
    pad = lhash + ps + x01 + m
    s10 = int(MGF(hex(r)[2 : len(hex(r)) - 1], k0 + k1 + k2 + 1), 16) ^ int(pad, 16)
    s16 = hex(s10)[2 : len(hex(s10)) - 1]
    t10 = int(MGF(s16, k0), 16) ^ r
    t16 = hex(t10)[2 : len(hex(t10)) - 1]
    w16 = x00 + t16 + s16
    w10 = int(w16, 16)
    str = hex(RSAEnc(w10, n, e))
    return str[2 : len(str) - 1]

def RSAOAEPDec(c, mLen, n, d, r):
    k = int(math.ceil(size(n) / 8))
    k0 = int(math.ceil(size(r) / 8))
    k2 = mLen
    k1 = k - 2 * k0 - k2 - 2
    w10 = RSADec(int(c, 16), d, n)
    s10 = (pow(2, 8 * (k0 + k1 + k2 + 1)) - 1) & w10
    t10 = (pow(2, 8 * k0) - 1)  &  (w10 >> 8 * (k0 + k1 + k2 + 1)) 
    rr = int(MGF(hex(s10)[2 : len(hex(s10)) - 1], k0), 16)  ^ t10
    if r !=  rr:
        return False
    pad10 = int(MGF(hex(rr)[2 : len(hex(rr)) - 1], k0 + k1 + k2 + 1) , 16) ^ s10 
    pad = hex(pad10)[2 : len(hex(pad10)) - 1]
    m = (pow(2, 8 * k2) - 1) & pad10
    lhash = (pow(2, 8 * k0) - 1) & pad10 >> 8 * (k1 + k2 + 1) 
    if hex(lhash)[2 : len(hex(lhash)) - 1] != hashlib.sha1().hexdigest():
        return False
    return hex(m)[2 : len(hex(m)) - 1]


if __name__ == "__main__":
#    print MGF("19910813", 21)
#    print HexstringToCharacters("1234")
#    print HexstringToCharacters("12345")
    p = 11853085763133505990286201269363921131755361282207771806454216823906463045956110404018518118871988561332197770015175458025096566875663947404231597048649687
    q = 13241479879786700069537673013402283713461303895018638725043715728333351182535991791698730454905679569343041660910401104499998964541968688709360528771269943
    n = p * q
    e = 16906953396398285955
    d = 724312013274593559104718233668131011194996096397911006981852189172961239048948863282836141926358773822231408712979119342947633487509489681999208855556699754187911367602954918028434935166295469845715934583725830138105140714265139027719788715269467483599026617823666098202900871395864967128743435198316095145
    r = 788255724614721016190591162463944054696650907899
    m = "8a97adebda4bc65e072c25a870dd939e"
    mLen = len(m) / 2 
    print RSAOAEPEnc(m, mLen, n, e, r)
    print RSAOAEPDec(RSAOAEPEnc(m, mLen, n, e, r), mLen, n, d, r)
