# import json

# from flask import Flask
# from flask_httpauth import HTTPBasicAuth
# from werkzeug.security import generate_password_hash, check_password_hash


# # user = {
# #     "user": generate_password_hash("password", salt_length=6)
# # }

# # with open('auth.dev.txt', mode='w') as file:
# #     s = json.dumps(user)
# #     file.write(s)

# with open('api/auth.dev.txt', mode='r') as file:
#     users = json.load(file)
#     pw = users.get('user')
#     print(pw)


"""script to run on raspberry pi to generate and post data"""
from datetime import datetime as dt
import json
import time
import random
import logging

import requests

logging.basicConfig(filename='chanch.log', filemode='w', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def shape_data():
    """pull data and convert temperature to Fahrenheit"""
    raw = random.uniform(20, 22)
    raw_c = (raw * (9/5)) + 32
    temp = round(raw_c, 1) - 6
    now = dt.now()
    return temp, now

def send_temp_point():
    """post temperature data to db api"""
    temp, now = shape_data()
    data_dict = {'temperature': temp, 'time': now}
    j = json.dumps(data_dict, indent=4, default=str)
    response = requests.post(
        'http://0.0.0.0:8100/post',
        json=j,
        auth=('user', 'password'), timeout=1.0)
    msg = response.text
    logging.debug(msg)

starttime = time.time()
while True:
    send_temp_point()
    time.sleep(10.0 - ((time.time() - starttime) % 10.0))
