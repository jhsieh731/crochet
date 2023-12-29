from flask import flash, redirect, render_template, request, g
from app import app, db, engine
from app.models import User

# !!! to run a CRUD operation: use ORM SQLAlchemy !!!

# routes
@app.route('/')
def home():
  return 'hi'
