from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder='../templates')

# Configure the database URL
drivername = "mysql+pymysql"
port = 3306
db_url = f"{drivername}://{os.getenv('USERNAME')}:{os.getenv('PASSWORD')}@{os.getenv('HOST')}:{port}/crochet"
# print(db_url)

# Configure Flask to use the database
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

# Create engine
engine = create_engine(db_url)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
# models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

# in flask shell: db.create_all()