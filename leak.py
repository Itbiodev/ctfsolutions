import telnetlib
import json
from base64 import b64decode

HOST = "socket.cryptohack.org"
PORT = 13370

tn = telnetlib.Telnet(HOST,PORT)
bucket = []

def json_send(msg):
    request = json.dumps(msg).encode()
    tn.write(request)

def json_recv():
    line = readline()
    return json.loads(line.decode())

def readline():
    return tn.read_until(b"\n")

readline()

json_send({"msg":"request"})
received = json_recv()
ct = received["ciphertext"]

while len(bucket) < 74:
    json_send({"msg":"request"})
    received = json_recv()
    try:
        ct = received["ciphertext"]
        print(ct)
        c = list(b64decode(ct))[0]
        if c not in bucket and c > 47 and c < 123:
            bucket.append(list(b64decode(ct))[0])
    except:
        pass
print(bucket)


