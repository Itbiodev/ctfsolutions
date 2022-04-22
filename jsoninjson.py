import json

username = "|"
body = '{' \
+ '"admin": "' + "False" \
+ '", "username": "' + str(username) \
+ '"}'

json.loads(body)