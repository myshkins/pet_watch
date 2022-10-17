from flask import Blueprint, render_template
from flask import current_app as app
from flask import Blueprint, render_template
from flask import current_app as app
import requests

about_bp = Blueprint(
    'about_bp', __name__,
    template_folder='templates',
    static_folder='static')

@about_bp.route('/about', endpoint='about', methods=['GET'])
def about():
    return render_template('index.html')



