import random
from datetime import datetime as dt
import json
import time
import requests



def send_temp_point():
    temp = random.uniform(60.0, 70.0)
    now = dt.now()
    data_dict = {'temperature': temp, 'time': now}
    j = json.dumps(data_dict, indent=4, default=str)
    response = requests.post(
        'http://0.0.0.0:8100/post',
        json=j, auth=('user', 'password'), timeout=.1)
    print(response.text)

starttime = time.time()
while True:
    send_temp_point()
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))
