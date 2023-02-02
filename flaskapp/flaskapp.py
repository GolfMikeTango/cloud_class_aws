from flask import Flask, Blueprint
from . import db

flaskapp = Blueprint('flaskapp', __name__)

@flaskapp.route('/')
def index():
    return 'Index'

@flaskapp.route('/profile')
def profile():
    return 'profile'

@flaskapp.route('/upload-display')
def upload():
    return 'upload or display page'