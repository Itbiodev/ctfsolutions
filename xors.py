from Crypto.Util.number import long_to_bytes
#KEY1 
a = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
#KEY2 ^ KEY1
b = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
#KEY2 ^ KEY3 
c = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
#FLAG ^ KEY1 ^ KEY3 ^ KEY2 
d = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

#flag = d^c^a
#print(long_to_bytes(flag).decode('utf-8')) 
##########################################################
flag = 0x73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
print(long_to_bytes(flag).decode('utf-8'))
for byte in long_to_bytes(flag):
    print(chr(byte^16),end="")
else:
    print("")
##########################################################
flag = 0x0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
y = list(long_to_bytes(flag))
x = []
for char in "crypto{}":
    print(ord(char),end=",")
    x.append(ord(char))
else:
    print("")
u = [14, 11, 33, 63, 38, 4, 30,4]

def bytes_xor(a,b):
    return [(a^b) for a,b in zip(a,b)]

key = bytes_xor(x,u)

def bytes_xor_char(a,b):
    return "".join([chr(a^b) for a,b in zip(a,b)])

key = bytes_xor(x,u)
k = "myXORkey"

z = []
for i in range(5):
    z.append(bytes_xor_char(y[i*8:(i+1)*8], key))
z.append(bytes_xor_char(y[40:42],key[0:2]))

print("".join(z))
#####################################################
b = []
with open("lemur.png","rb") as f1:
    while byte:
        b.append(f1.read(1))

print(b)