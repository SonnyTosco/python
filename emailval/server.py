from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
    print "g2g"
    query = "SELECT * FROM emaildb"                           # define your query
    email = mysql.query_db(query)
    return render_template("index.html")
@app.route('/friends', methods=['POST'])
def submit():
    data=request.form
    print "Gucci"
    if len(data['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(data['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")
    print "Carter4"
    print request.form['email']
    query = "INSERT INTO friends (email, created_at, updated_at)\
             VALUES (:email, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'email': request.form['email']
           }
    mysql.query_db(query, data)
    session['email'].insert(0, {'color':'green','text':'The email you entered\
    {} is a valid email address.\
    from the {}! ({})'.format(request.form['email'], strftime("%Y/%m/%d %I:%M %p").lower())})
    return render_template("result.html")
app.run(debug=True)
