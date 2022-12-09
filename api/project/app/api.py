"""api routes"""
from datetime import datetime as dt
from datetime import timedelta
import json

from flask import make_response, request
from flask import current_app as app
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash


from models import db, Temp


auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    with open('auth.txt', mode='r') as file:
        users = json.load(file)
        if username in users and check_password_hash(users.get(username), password):
            return username

def trim_data():
    """removes old, unneccesary data"""
    cutoff = dt.now() - timedelta(seconds=50)
    old_data = db.session.execute(
        db.select(Temp).where(Temp.time <= cutoff)
        ).scalars()
    for row in old_data:
        db.session.delete(row)
    db.session.commit()


@app.route('/post', endpoint='post', methods=['POST'])
@auth.login_required
def make_temp_point():
    """api post function for receiving and storing temperature data"""
    string_data = request.get_json()
    json_data = json.loads(string_data)
    temp = round(float(json_data['temperature']), 1)
    time = dt.strptime(json_data['time'], '%Y-%m-%d %H:%M:%S.%f')
    temp_point = Temp(temperature=temp, time=time)
    trim_data()
    db.session.add(temp_point)
    db.session.commit()
    return json_data
