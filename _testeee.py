import json

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


# user = {
#     "user": generate_password_hash("password", salt_length=6)
# }

# with open('auth.dev.txt', mode='w') as file:
#     s = json.dumps(user)
#     file.write(s)

with open('api/auth.dev.txt', mode='r') as file:
    users = json.load(file)
    pw = users.get('user')
    print(pw)
