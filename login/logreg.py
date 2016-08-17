from flask import Flask, request, render_template, redirect, session
from mysqlconnection import MySQLConnector
import datetime
now = datetime.datetime.now()
app = Flask(__name__)
mysql = MySQLConnector(app, 'fullfriend')
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
    pass

@app.route('/add')
def add():
    pass

@app.route('/reg', methods=['POST'])
def create():
    pass
