from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

SECRET_KEY = 'Sup3r$3cretkey'
UPLOAD_FOLDER = '/app/static/uploads'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://proj1:password123@localhost/proj1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
db = SQLAlchemy(app)

app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
from app import views
