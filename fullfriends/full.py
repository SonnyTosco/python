from flask import Flask, request, render_template, redirect, session
from mysqlconnection import MySQLConnector
import datetime
now = datetime.datetime.now()
app = Flask(__name__)
mysql = MySQLConnector(app, 'fullfriend')
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
    query="SELECT * FROM friends"
    session['time']=now.strftime("%Y-%m-%d %H:%M")
    print "g2g"
    return render_template("index.html", friends=mysql.query_db(query))

@app.route('/add')
def add():
    return render_template("add.html")

#Handle the add friend form submit and create the friend in the DB
@app.route('/friends', methods=['POST'])
def create():
    print request.form['fname']
    print request.form['lname']
    print request.form['email']
    query = "INSERT INTO friends (fname, lname, email, created_at, updated_at)\
             VALUES (:fname, :lname, :email, NOW(), NOW())"
    data = {
             'fname': request.form['fname'],
             'lname':  request.form['lname'],
             'email':  request.form['email']
           }
    mysql.query_db(query, data)
    return redirect('/')

#Display the edit friend page for the particular friend
@app.route('/friends/<id>/edit', methods=['GET'])
def edit(id):
    return render_template("edit.html", id=id)

#Handle the edit friend form submit and update the friend in the DB
@app.route('/friends/<id>', methods=['POST'])
def update(id):
    print "change clothes"
    query = '''UPDATE friends SET fname=:fname, lname=:lname, email=:email
                WHERE id=:id'''
    data = {
        'id': id,
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    print "and go"
    mysql.query_db(query, data)
    return redirect('/')

#Delete the friend from the DB
@app.route('/friends/<id>/delete', methods=['GET'])
def destroy(id):
    print "Luke"
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    print "Skywalker"
    return redirect('/')
app.run(debug=True)




# # this will load a page that has 2 forms one for registration and login
# @app.route('/', methods=['GET'])
# def index():
#  return render_template('index.html')
#
# # we are going to add functions to create new users and login users
# @app.route('/create_user', methods=['POST'])
# def create_user():
#  email = request.form['email']
#  username = request.form['username']
#  password = request.form['password']
#  # run validations and if they are successful we can create the password hash with bcrypt
#  pw_hash = bcrypt.generate_password_hash(password)
#  # now we insert the new user into the database
#  insert_query = "INSERT INTO users (email, username, pw_hash, created_at) VALUES (:email, :username, :pw_hash, NOW())"
#  query_data = { 'email': email, 'username': username, 'pw_hash': pw_hash }
#  mysql.query_db(insert_query, query_data)
#  # redirect to success page
#
# @app.route('/login', methods=['POST'])
# def login():
#  email = request.form['email']
#  password = request.form['password']
#  user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
#  query_data = { 'email': email }
#  user = mysql.query_db(user_query, query_data) # user will be returned in a list
#  if bcrypt.check_password_hash(user[0]['pw_hash'], password):
#   # login user
#  else:
#   # set flash error message and redirect to login page
