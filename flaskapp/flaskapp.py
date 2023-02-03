from flask import Flask, Blueprint, render_template
from flask_login import login_required, current_user
from . import db

flaskapp = Blueprint('flaskapp', __name__)

@flaskapp.route('/')
def index():
    return render_template('index.html')

@flaskapp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@flaskapp.route('/upload-display')
def upload():
    return 'upload or display page'