from flask import Flask, request, render_template
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'my_database_here')

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/friends', methods=['POST'])
def create():
    pass

@app.route('/friends/<id>/edit', methods=['GET'])
def edit(id):
    pass

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    pass

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    pass





# this will load a page that has 2 forms one for registration and login
@app.route('/', methods=['GET'])
def index():
 return render_template('index.html')

# we are going to add functions to create new users and login users
@app.route('/create_user', methods=['POST'])
def create_user():
 email = request.form['email']
 username = request.form['username']
 password = request.form['password']
 # run validations and if they are successful we can create the password hash with bcrypt
 pw_hash = bcrypt.generate_password_hash(password)
 # now we insert the new user into the database
 insert_query = "INSERT INTO users (email, username, pw_hash, created_at) VALUES (:email, :username, :pw_hash, NOW())"
 query_data = { 'email': email, 'username': username, 'pw_hash': pw_hash }
 mysql.query_db(insert_query, query_data)
 # redirect to success page

@app.route('/login', methods=['POST'])
def login():
 email = request.form['email']
 password = request.form['password']
 user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
 query_data = { 'email': email }
 user = mysql.query_db(user_query, query_data) # user will be returned in a list
 if bcrypt.check_password_hash(user[0]['pw_hash'], password):
  # login user
 else:
  # set flash error message and redirect to login page
