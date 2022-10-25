import json
from datetime import datetime as dt
from datetime import timedelta
import requests
import base64
from werkzeug.security import generate_password_hash, check_password_hash

temp = 72.4
now = str(dt.now())
data_dict = {'temperature': temp, 'time': now}
j = json.dumps(data_dict, default=str)
print(j)
response = requests.post('http://www.pet-watch.ak0.io/post', json=j, auth=('myshkins', 'iw4GD^5EZfH*SDTr%wtpm$Ni8'))
print(response)
print(response.text)

# now = str(dt.now())
# t = dt.strptime(now, '%Y-%m-%d %H:%M:%S.%f')
# print(t)

# pw = 'iw4GD^5EZfH*SDTr%wtpm$Ni8'
# hsh = generate_password_hash(pw, method="pbkdf2:sha256", salt_length=8)
# print(hsh)
# chkhsh = 'pbkdf2:sha256:260000$uawPFBxAbiz4ZHC8$fec1a0d3a4895308b3eca839dd3471a58036d5a392b6650c04bc786a80001d5c'
# print(check_password_hash(hsh, pw))


# from flask import Flask, request, jsonify

# app = Flask(__name__)


# auth_cyph = "bXlzaGtpbnM6d29yZHBhc3M="
# decyph = base64.b64decode(auth_cyph).decode("utf-8")
# print(decyph)

