from flask import Flask, request, render_template, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
import datetime
now = datetime.datetime.now()
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app, 'logandreg')
bcrypt = Bcrypt(app)
app.secret_key = "ThisIsSecret!"

#Index
@app.route('/', methods=['GET'])
def index():
    pass

#Route for after successful creation
@app.route('/paulwall', methods=['GET'])
def wall():
    pass

#Add a new user
@app.route('/create', methods=['POST'])
def create():
    pass

#Login existing user
@app.route('/user', methods=['POST'])
def login():
    pass

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
