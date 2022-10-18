from flask import jsonify, Blueprint, make_response
from flask import current_app as app
from datetime import datetime as dt
from datetime import timedelta
from project.models import db, Temps



## Blueprint Config
api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/hi', endpoint='say_hi', methods=['GET'])
def say_hi():
    return jsonify("hellow")


@api_bp.route('/make_temp_point', endpoint='make_temp_point', methods=['POST'])
def make_temp_point():
    data = Temps.query.all()    #clear temperature rows older than needed time window
    for row in data:
        now = dt.now()
        if (now - row.time) > timedelta(days=8):
            db.session.delete(row)
            db.session.commit()
    temp_h = sense.get_temperature_from_humidity()
    temp_p = sense.get_temperature_from_pressure()
    temp_mean = (temp_h + temp_p) / 2
    time = dt.now()
    new_t_point = Temps(temperature=temp_mean, time=time)
    db.session.add(new_t_point)
    db.session.commit()
    return {
        "time": time,
        "temperature": temp_mean
    }
