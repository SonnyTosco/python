from flask import Flask, request, render_template, redirect, session
from mysqlconnection import MySQLConnector
import datetime
now = datetime.datetime.now()
app = Flask(__name__)
mysql = MySQLConnector(app, 'fullfriend')
app.secret_key = "ThisIsSecret!"

#Index
@app.route('/', methods=['GET'])
def index():
    pass

#routes back to index after you created a user
@app.route('/add', methods=['GET'])
def add():
    pass

#creates an account
@app.route('/reg', methods=['POST'])
def create():
    pass

#after login, checks to see if its valid in db
@app.route('/reg', methods=['POST'])
def create():
    pass

#destination after a successful login
@app.route('/reg', methods=['POST'])
def create():
    pass
