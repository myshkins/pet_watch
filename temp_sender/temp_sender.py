"""script to run on raspberry pi to generate and post data"""
from datetime import datetime as dt
import json
import time

from sense_hat import SenseHat
import requests

sense = SenseHat()

def get_temp_h():
    """get temperature from humidity sensor"""
    temp_h = sense.get_temperature_from_humidity()
    return temp_h

def get_temp_p():
    """get temperature from pressure sensor"""
    temp_p = sense.get_temperature_from_pressure()
    return temp_p

def shape_data():
    """pull data and convert temperature to Fahrenheit"""
    temp_h = get_temp_h()
    temp_h = (temp_h * (9/5)) + 32
    temp_p = get_temp_p()
    temp_p = (temp_p * (9/5)) + 32
    temp = round(((temp_h + temp_p) / 2), 1) - 6
    now = dt.now()
    return temp, now

def send_temp_point():
    """post temperature data to db api"""
    temp, now = shape_data()
    data_dict = {'temperature': temp, 'time': now}
    j = json.dumps(data_dict, indent=4, default=str)
    response = requests.post(
        'https://www.pet-watch.ak0.io/post',
        json=j,
        auth=('user', 'password'), timeout=1.0)

starttime = time.time()
while True:
    send_temp_point()
    time.sleep(600.0 - ((time.time() - starttime) % 600.0))
