import os

from flask import request, Blueprint, render_template

greeting_bp = Blueprint('greeting', __name__)


@greeting_bp.route('/home', methods=['GET', 'POST'])
@greeting_bp.route('/', methods=['GET', 'POST'])
def greeting():
    if request.method=="POST":
        user_name = request.form['user_name']
        return render_template('home.html', user_name=user_name)
    return render_template('home.html')
