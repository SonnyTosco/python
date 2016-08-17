from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re
import datetime
now = datetime.datetime.now()
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'emaildb')
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
    print "g2g"
    # query = "SELECT * FROM emails"                           # define your query
    # emaildb = mysql.query_db(query)
    return render_template("index.html")

@app.route('/friends', methods=['POST'])
def submit():
    print "Gucci"
    data=request.form
    print data ['email']
    if len(data['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(data['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")
        query = "INSERT INTO emails (email, created_at, updated_at)\
                 VALUES (:email, NOW(), NOW())"
        data = {
                 'email': data['email']
               }
        mysql.query_db(query, data)
        session['email']=data['email']
        session['time']=now.strftime("%Y-%m-%d %H:%M")
        return redirect("/result")
    print "Carter4"
    return redirect('/')

@app.route('/result')
def result():
    print session['email']
    print session['time']
    return render_template("result.html")
app.run(debug=True)
