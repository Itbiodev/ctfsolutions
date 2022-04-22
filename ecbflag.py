from Crypto.Cipher import AES
import hashlib

with open("pass.txt") as f:
    words = [w.strip() for w in f.readlines()]

def decrypt(ct, word):
    ciphertext = bytes.fromhex(ct)
    key = hashlib.md5(word.encode()).digest()
    #key = bytes.fromhex(keyw)
    cipher = AES.new(key, AES.MODE_ECB)
    flag = cipher.decrypt(ciphertext)
    return flag

for word in words:
    print(decrypt("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66",word))
