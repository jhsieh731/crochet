from flask import Flask, flash, redirect, render_template, request, g
import pymysql
import atexit

app = Flask(__name__)

# configure db connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''

mysql = pymysql.connect(host=app.config['MYSQL_HOST'],
                             user=app.config['MYSQL_USER'],
                             password=app.config['MYSQL_PASSWORD'],
                             database='crochet',
                             cursorclass=pymysql.cursors.DictCursor,
                             autocommit=True)

db = mysql.cursor()

@app.before_request
def open_connection():
  g.db = mysql.cursor()

@app.after_request
def close_connection():
  g.db.close()

# !!! to run a CRUD operation: g.db.execute('SELECT (%s, %s) FROM ...', (var_1, var_2)) !!!
# note: can also use dictionary as vars: g.db.execute("SELECT %var_name FROM ..."", {var_name: value})

# db clean-up on server close
def close_db():
  mysql.close()
atexit.register(close_db)

# routes
@app.route("/", methods=[])
def home():
  return render_template('index.html')

if __name__ == "__main__":
  app.run(debug = True)