from flask import Blueprint, render_template, redirect, url_for
from flask import current_app as app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from project.models import db, User
import requests
import json



home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static')


class UserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Register")


@home_bp.route('/', endpoint='home', methods=['GET', 'POST'])
def home():
    form = UserForm()
    if form.is_submitted():
        user = User()
        user.username = form.name.data
        user.email = form.email.data
        user.password = form.password.data #generate_password_hash(form.password.data, method="pbkdf2:sha256", salt_length=8)
        db.session.add(user)
        db.session.commit()
        return render_template("index.html", form=form)
    return render_template("index.html", form=form)



@home_bp.route('/say_hi', endpoint='say_hi', methods=['GET'])
def say_hi():
    response = requests.get('http://192.168.86.23:8000/say_hi')
    print(response.text)
    return redirect(url_for('home_bp.home'))


# @temp_bp.route('/get_all', endpoint='get_all', methods=['GET'])
# def get_all():
#     query = Temps.query.all()
#     data = {}
#     for point in query:
#         ptime = str(point.time)
#         data[ptime] = [point.temperature]
#     return jsonify(data)

# @temp_bp.route('/get_day', endpoint='get_day', methods=['GET'])
# def get_day():
#     query = Temps.query.all()
#     data = {}
#     now = dt.now()
#     for point in query:
#         if (now - point.time) < timedelta(days=1):
#             ptime = str(point.time)
#             data[ptime] = [point.temperature]
#     return jsonify(data)
