from datetime import datetime as dt
from datetime import timedelta
from sense_hat import SenseHat
import json
import time
import requests
import os
import random
# import logging

sense = SenseHat()

# logging.basicConfig(filename='pi_temp_sender.log', )
def get_temp_h():
    temp_h = random.uniform(15.1, 16.1)
    temp_h = sense.get_temperature_from_humidity()
    return temp_h

def get_temp_p():
    temp_p = random.uniform(15.1, 16.1)
    temp_p = sense.get_temperature_from_pressure()
    return temp_p

def make_temp_point():
    temp_h = get_temp_h()
    temp_h = (temp_h * (9/5)) + 32
    temp_p = get_temp_p()
    temp_p = (temp_p * (9/5)) + 32
    temp = round(((temp_h + temp_p) / 2), 1) - 6
    now = dt.now()
    data_dict = {'temperature': temp, 'time': now}
    j = json.dumps(data_dict, indent=4, default=str)
    response = requests.post(
        'https://www.pet-watch.ak0.io/post',
        json=j,
        auth=('myshkins', 'password'))



starttime = time.time()

while True:
    make_temp_point()
    time.sleep(600.0 - ((time.time() - starttime) % 600.0))


