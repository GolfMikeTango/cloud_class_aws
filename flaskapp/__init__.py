from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # Create blueprint for flaskapp (our main file)
    from .flaskapp import flaskapp as main_blueprint
    app.register_blueprint(main_blueprint)

    # Create blueprint for authentication
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
