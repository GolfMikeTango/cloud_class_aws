from flask import Flask, Blueprint
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/test')
def test():
    return 'Test works!'

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('/logout')
def logout():
    return 'Logout'