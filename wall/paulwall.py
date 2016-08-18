from flask import Flask, request, render_template, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
import datetime
now = datetime.datetime.now()
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app, 'wall')
bcrypt = Bcrypt(app)
app.secret_key = "ThisIsSecret!"

#Index
@app.route('/', methods=['GET'])
def index():
    print "Cash Money taking over for the 9-9 and 2000"
    return render_template("index.html")

#Route for after successful creation
@app.route('/paulwall', methods=['GET'])
def wall():
    print "Slab God"
    return render_template("paulwall.html")

#Add a new user
@app.route('/create', methods=['POST'])
def create():
    data=request.form
    password = bcrypt.generate_password_hash(data['password'])
    print data['fname']
    print data['lname']
    print data['email']
    print password
    if len(data['email'])<1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(data['email']):
        flash("Invalid Email Address!")
    elif not (data['password'] == data['c_password']):
        flash("Passwords do not match")
    else:
        query = "INSERT INTO users (fname, lname, email, password, created_at, updated_at)\
                 VALUES (:fname, :lname, :email, :password, NOW(), NOW())"
        data = {
                 'fname': data['fname'],
                 'lname':  data['lname'],
                 'email':  data['email'],
                 'password':  password,
               }
        mysql.query_db(query, data)
        return redirect("/paulwall")
    print "Degreez"
    return redirect('/')

#Login existing user
@app.route('/user', methods=['POST'])
def login():
    print "Get your"
    data=request.form
    if (data['email'] and data['password']):
        query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
        data1 = {
                 'email':  data['email'],
               }
        email=mysql.query_db(query, data1)
        print "g2g email"
        if (len('email'))<1:
            print "passed length validation, line 69"
            flash("Email isn't on file")
            return redirect('/')
        else:
            print "line 76, entered pw", data['password']
            print "bcrypt methods, line 77:", dir(bcrypt)
            if bcrypt.check_password_hash(email[0]['password'], data['password']):
                print "pw from db, line 77", email[0]['password']
                return redirect('/paulwall')
            else:
                print "failed validation, line 80"
                flash("password not correct")
                return redirect('/')
    print "roll on"
    return redirect('/')

#create POST
@app.route('/post', methods=['POST'])
def post():
    pass

#create comment
@app.route('/comment', methods=['POST'])
def comment():
    pass

#delete post
@app.route('/dpost', methods=['GET'])
def dpost():
    pass

#delete comment
@app.route('/dcomment', methods=['GET'])
def dcomment():
    pass

#logout
@app.route('/logout', methods=['GET'])
def logout():
    pass

app.run(debug=True)
