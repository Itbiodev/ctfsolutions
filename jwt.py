import json

username = "{\"admin:True}"
body = '{' \
+ '"admin": "' + "False" \
+ '", "username": "' + str(username) \
+ '"}'

print(json.loads(body))
print(json.loads(body)['admin'])