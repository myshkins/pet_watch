from flask import jsonify, Blueprint, make_response, request, abort
from flask import current_app as app
from datetime import datetime as dt
from datetime import timedelta
from project.models import db, Temps
import json
from werkzeug.security import generate_password_hash, check_password_hash
import base64



## Blueprint Config
api_bp = Blueprint('api_bp', __name__)


# @api_bp.route('/hi', endpoint='say_hi', methods=['GET'])
# def say_hi():
#     return jsonify("hellow")


@api_bp.route('/post', endpoint='post', methods=['POST'])
def make_temp_point():
    auth_cyph = request.headers['Authorization'][6:]
    decyph = base64.b64decode(auth_cyph).decode("utf-8").split(":")
    with open('auth.txt') as file:
        pw_hash = file.read()
    if decyph[0] != 'myshkins' or not check_password_hash(pw_hash, decyph[1]):
        abort(401)
    else:
        j = request.get_json()
        data = json.loads(j)
        temp = data['temperature']
        time = dt.strptime(data['time'], '%Y-%m-%d %H:%M:%S.%f')
        data = Temps.query.all()    #clear temperature rows older than needed time window
        for row in data:
            if (now - row.time) > timedelta(days=8):
                db.session.delete(row)
                db.session.commit()
        new_t_point = Temps(temperature=temp, time=time)
        db.session.add(new_t_point)
        db.session.commit()
        return make_response()
