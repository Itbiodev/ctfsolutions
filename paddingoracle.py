import base64
from base64 import b64decode, b64encode
import requests
import sys, getopt
from Crypto.Random import get_random_bytes

def bytes_xor(s1,s2):
    return bytes([a^b for a,b in zip(s1,s2)])

def PaddingOracle(ct_bytes):
    url = "http://35.190.155.168/dcc2ed6138/?post"
    ct = b64encode(ct_bytes).decode('utf-8')
    ct = str(ct).replace('=', '~').replace('/', '!').replace('+','-')
    response = requests.get(url+'='+ct)
    if "PaddingException" not in response.text:
        print(ct)#remove if you don't want to see the progress
        result = 1
    else:
        result = 0
    return result

def BlockOracle(block):
    r = get_random_bytes(16)
    r = list(r)
    DecryptedBytes = [0]*16
    for j in range(16):
        for i in range(256):
            r[15-j] = i
            if j == 0:
                if PaddingOracle(bytes(r)+block):
                    DecryptedBytes[15-j] = i^(j+1)
                    break
            if j > 0:
                for k in range(j):
                    r[15-k] = DecryptedBytes[15-k]^(j+1)
                if PaddingOracle(bytes(r)+block):
                    DecryptedBytes[15-j] = i^(j+1)
                    break
    return DecryptedBytes

baseurl = "http://35.190.155.168/dcc2ed6138/?post=R1owgcD8JOkIZbe7rOvKCxQK7BBbOzQArurGaXyGi5IqBqw2Sk!oB9N3QI0waYnADTYWIgclwyKCP6rKFdjJfKmaVIkqz!SHZiWkhL0ukeZsbYO4eb7GaxPHlqJnQleeRP4ZERUBi4FLDLqeSL6gZzpL9LogQ5uCp34z8UXJyaty8izIUelToHEtw1ndSYX4jjGFWRct-xkrAY9eTWIcbw~~"
ct = baseurl.split('=')[1]
#ct = "U0ZqOBLZOF-lYIoglc7JHg~~"
ct_bytes = b64decode(ct.replace('~', '=').replace('!', '/').replace('-', '+'))
ct_list = list(ct_bytes)
n = int(len(ct_list)/16) #No. of blocks
blocks = [b'\x00']*n
for i in range(0,n):
    blocks[i] = bytes(ct_list[16*i:16*(i+1)])
    print(bytes_xor(BlockOracle(blocks[i]),blocks[i-1]))
