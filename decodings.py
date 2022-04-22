import telnetlib
import json
from base64 import b64decode
from Crypto.Util.number import bytes_to_long, long_to_bytes
import codecs

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST,PORT)

def json_send(msg):
    request = json.dumps(msg).encode()
    tn.write(request)

def json_recv():
    line = readline()
    return json.loads(line.decode())

def readline():
    return tn.read_until(b"\n")

def decoder(encoding, value):
    decoded =''
    if encoding == "base64":
        decoded = b64decode(value).decode()
    elif encoding == "rot13":
        decoded = codecs.decode(value, 'rot_13')
    elif encoding == "utf-8":
        decoded = ''.join([chr(a) for a in value])
    elif encoding == "hex":
        decoded = bytearray.fromhex(value).decode() 
    elif encoding == "bigint":
        decoded = long_to_bytes(int(value,16)).decode()
    return {"decoded": decoded}
count = 0
while count < 110:
    msg = json_recv()
    print(msg)
    json_send(decoder(msg['type'],msg['encoded']))
    count = count + 1
