from base64 import b64decode

with open("leaky.txt") as f:
    cts = [b64decode(w.strip()) for w in f.readlines()]

for i in range(20):
    bucket = []
    for ct in cts:
        if list(ct)[i] not in bucket:
            bucket.append(list(ct)[i])
    for b in range(len(bucket)):
        if b not in bucket:
            print(i,end=":")
            print(chr(b),end=",")
else:
    print(" ")
