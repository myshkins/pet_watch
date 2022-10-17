from datetime import datetime as dt
from datetime import timedelta
from sense_hat import SenseHat
import json
import time
import requests
import logging
import os


sense = SenseHat()


logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

# logging.basicConfig(filename='chanch_db_builder.log', encoding='utf-8', level=logging.WARNING, format='%(asctime)s %(message)s')


def get_temp_h():
    temp_h = sense.get_temperature_from_humidity()
    return temp_h

def get_temp_p():
    temp_p = sense.get_temperature_from_pressure()
    return temp_p

def make_temp_point():
    temp_h = sense.get_temperature_from_humidity()
    temp_p = sense.get_temperature_from_pressure()
    temp_mean = (temp_h + temp_p) / 2
    time = dt.now()
    #make post requester here
    response = requests.post(url)
    #sc = response.status_code
    #if sc != 200:
    #logging.warning('something went wrong, response code %d' %sc)
    return


starttime = time.time()

while True:
    make_temp_point()
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))


