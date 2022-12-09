"""app route view functions"""
import base64
from io import BytesIO
from datetime import datetime as dt
from datetime import timedelta
import logging

from flask import Blueprint, render_template
from matplotlib.figure import Figure
import matplotlib.dates as mdates
import numpy as np

from models import db, Temp


logging.basicConfig(filename='chanch.log', filemode='w', level=logging.DEBUG)
logger = logging.getLogger(__name__)

home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static')

def get_current_temp():
    data = db.session.execute(
        db.select(Temp).order_by(Temp.time.desc())).fetchone()
    if data is None:
        temp = "None"
    else:
        temp = data[0].temperature
    return temp

def get_day():
    cutoff = dt.now() - timedelta(hours=24)
    data = db.session.execute(
        db.select(Temp).where(Temp.time >= cutoff)
        ).scalars()
    times, temps = [], []
    for row in data:
        times.append(str(row.time))
        temps.append([row.temperature])
    return (times, temps)

def make_arrays(data):
    times_arr = np.asarray(data[0], dtype=np.datetime64)
    temp_arr = np.asarray(data[1])
    return (times_arr, temp_arr)

@home_bp.route('/', endpoint='home', methods=['GET'])
def home():
    curr_temp = get_current_temp()
    times, temps = make_arrays(get_day())
    fig = Figure()
    ax = fig.subplots()
    ax.plot(times, temps, label='temps', marker=",")
    ax.xaxis.set_major_locator(mdates.HourLocator(byhour=range(24), interval=4))
    formatter = mdates.DateFormatter("%H:%M")
    ax.xaxis.set_major_formatter(formatter)
    ax.set_xlabel('TIME')
    ax.set_ylabel('TEMP')
    ax.set_facecolor('#D0F8FF')
    for label in ax.get_xticklabels():
            label.set_rotation(40)
            label.set_horizontalalignment('right')
    ax.set_ylim(50, 85)
    ax.set_xlim(times[0], times[len(times)-1])
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight', pad_inches=.2)
    data_plot = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('index.html', curr_temp=curr_temp, data_plot=data_plot)