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
    return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
    data=request.form
    print "Gucci"
    #All fields are required and must not be blank
    if data==None:
        flash("ALL fields must be filled out")
    else:
        flash("")
    print "Carter"
    #First and Last name cannot contain any numbers
    if data['fname']==int:
        flash("No numbers, just letters")
    else:
        flash("Your name is unique!")
    print "Carter2"
    #Password should be more than 8 characters
    if data['pword'] < 8:
        flash("Passwords should be at least 8 characters")
    else:
        flash("Password is secure")
    print "Carter3"
    #Email should be a valid email
    if len(data['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(data['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")
    print "Carter4"
    #Password and Password confirmation should match
    if data['pword']==data['c_pword']:
        flash("Passwords match")
    else:
        flash("Passwords do not match")
    print "Carter5"
    return redirect('/')
app.run(debug=True)
