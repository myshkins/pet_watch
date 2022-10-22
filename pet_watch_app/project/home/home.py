from flask import Blueprint, render_template, redirect, url_for
from flask import current_app as app
import requests
import json
import base64
from io import BytesIO
from matplotlib.figure import Figure
import matplotlib.dates as mdates
import time
from datetime import datetime as dt
from datetime import timedelta
import numpy as np
from project.models import db, Temps



home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static')


def get_all():
    query = Temps.query.all()
    times, temps = [], []
    for point in query:
        times.append(str(point.time))
        temps.append([point.temperature])
    return (times, temps)

def get_day():
    now = dt.now()
    query = Temps.query.filter((now - Temps.time) < timedelta(days=1)).all()
    times, temps = [], []
    for point in query:
        times.append(str(point.time))
        temps.append([point.temperature])
    return (times, temps)

def make_arrays(data):
    date_arr = np.array(data[0], dtype='datetime64')
    temp_arr = np.array(data[1])
    return (date_arr, temp_arr)

def get_current_temp():
    temp = Temps.query.first().temperature
    return temp


@home_bp.route('/', endpoint='home', methods=['GET'])
def home():
    temp_now = round(get_current_temp(), 1)
    dates, temps = make_arrays(get_day())
    fig = Figure()
    ax = fig.subplots()
    ax.plot(dates, temps, label='temps', marker=",")
    ax.xaxis.set_major_locator(mdates.HourLocator(byhour=range(24), interval=4))
    formatter = mdates.DateFormatter("%H:%M")
    ax.xaxis.set_major_formatter(formatter)
    ax.set_xlabel('TIME') 
    ax.set_ylabel('TEMP')
    ax.set_facecolor('#D0F8FF')
    for label in ax.get_xticklabels():
            label.set_rotation(40)
            label.set_horizontalalignment('right')
    ax.set_ylim(40, 100)
    ax.set_xlim(dates[0], dates[len(dates)-1])
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight', pad_inches=.2)
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('index.html', temp_now=temp_now, data=data)


@home_bp.route('/say_hi', endpoint='say_hi', methods=['GET'])
def say_hi():
    response = requests.get('http://192.168.86.23:8000/say_hi')
    print(response.text)
    return redirect(url_for('home_bp.home'))
