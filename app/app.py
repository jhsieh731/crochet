from flask import flash, redirect, render_template, request, g
from app import app, db, engine, db_session, User

# generate tables: db.create_all()

# !!! to run a CRUD operation: use ORM SQLAlchemy !!!
# Recommended:
  #  session = db_session()  
  #  session.query(User).all() [or some other query]
  #  session.flush()
  #  session.close()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# routes
@app.route('/')
def home():
  return render_template('index.html')
