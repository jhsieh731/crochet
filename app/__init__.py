from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine.url import URL
import pymysql
from sqlalchemy import create_engine

app = Flask(__name__)

# configure db connection
HOST = 'localhost'
USERNAME = 'root'
PASSWORD = ''

# Configure the database URL
db_url = URL(
    drivername="mysql+pymysql",
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    database="crochet",
    port=3306,
    query={},
)
print(db_url)
# Configure Flask to use the database
app.config["SQLALCHEMY_DATABASE_URI"] = str(db_url)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

# Create engine
engine = create_engine(db_url)

# Import the models to make them available in the app
from app.models import User