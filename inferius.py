#!/usr/bin/env python3

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

e = 3

# n will be 8 * (100 + 100) = 1600 bits strong which is pretty good
while True:
    p = getPrime(100)
    q = getPrime(100)
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    if d != -1 and GCD(e, phi) == 1:
        break

n = p * q

flag = b"XXXXXXXXXXXXXXXXXXXXXXX"
pt = bytes_to_long(flag)
ct = pow(pt, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")
d = 494966086082978049281030458426104032709522303246720984637467
ct = 39207274348578481322317340648475596807303160111338236677373
n = 742449129124467073921545687640895127535705902454369756401331
pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
print(long_to_bytes(11515195063862319002386785506490949575337279649825636153248053928580408574830461))
