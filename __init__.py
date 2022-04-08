from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

"""This needs to be isolated to support blueprints and models"""
app = Flask(__name__)
dbURI = 'sqlite:///model/myDB.db'
# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy(app)
Migrate(app, db)

# The most important part of an application that uses Flask-Login is the LoginManager class.
# You should create one for your application like this:  
# Setup LoginManager object (app)
login_manager = LoginManager()

# The login manager contains the code that lets your application and Flask-Login work together, 
# such as how to load a user from an ID,  where to send users when they need to log in, and the like.  
# Once the actual application object has been created, you can configure it for login with:

login_manager.init_app(app)
