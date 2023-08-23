from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt, check_password_hash

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)


from app import routes, models