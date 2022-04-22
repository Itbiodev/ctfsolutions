from random import randint

a = 288260533169915
p = 1007621497415251

FLAG = b'crypto{????????????????????}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    #plaintext is binary of each letter ocupying 8 bits
    for b in plaintext:
        e = randint(1, p) # [1,p)
        n = pow(a, e, p) # a^e mod p
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    return ciphertext

# print(encrypt_flag(FLAG))

pt = '01100011011100100111100101110000011101000110111101111011011100000011010001110100011101000110010101110010011011100111001101011111001100010110111001011111011100100110010100110101011010010110010001110101001100110111001101111101'

blocks = []
for i in range(len(pt)//8):
    blocks.append(pt[8*i:8*(i+1)])

final = ''
for block in blocks:
    final += chr(int(block,2))

print(final)


