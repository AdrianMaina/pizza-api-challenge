# server/config.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instantiate the Flask app
app = Flask(__name__)

# Configure the database URI.
# Uses a relative path for the SQLite database file.
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Suppress the Flask-SQLAlchemy track modifications warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instantiate SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)