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
    data = 	{'user_id': session.get('user_id')}
    query = '''SELECT * FROM users
    			WHERE id = :user_id LIMIT 1
    		'''
    user = mysql.query_db(query, data)

    #messages
    query = '''SELECT message, messages.id as message_id,
    			messages.user_id as user_id,
    			CONCAT(users.fname, ' ', users.lname) as name,
                DATE_FORMAT(messages.created_at, '%M %D, %Y (%H:%i)') as message_date
    			FROM messages
    			LEFT JOIN users on messages.user_id = users.id
    			ORDER BY messages.created_at DESC
    		'''
    messages = mysql.query_db(query)

    #comments
    query = """SELECT comments.comment as comment, comments.id as comment_id,
				comments.message_id as message_id, comments.user_id as user_id,
				CONCAT(users.fname, ' ', users.lname) as name,
				DATE_FORMAT(comments.created_at, '%M %D, %Y (%H:%i )') as comment_date
				FROM comments
				LEFT JOIN users on comments.user_id = users.id
				ORDER BY comments.created_at ASC
			"""
    comments = mysql.query_db(query, data)
    for comment in comments:
        print comment['comment_id']
    return render_template("paulwall.html", user=user, messages=messages, comments=comments)

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
        data = 	{'user_id': session.get('user_id')}
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
            print email
            if bcrypt.check_password_hash(email[0]['password'], data['password']):
                print "pw from db, line 77", email[0]['password']
                session['user_id']=email[0]['id']
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
    print "line 88"
    print request.form
    query =   '''INSERT INTO messages (user_id, message, created_at, updated_at)
                VALUES (:id, :message, NOW(), NOW())'''
    print "line 91"
    data  = {
            'id':session['user_id'],
            'message': request.form['message']
    }
    print "line 96"
    mysql.query_db(query, data)
    print "line 98"
    return redirect('/paulwall')

#create comment
@app.route('/comment/<message_id>', methods=['POST'])
def comment(message_id):
    print "line 105"
    print request.form
    query='''INSERT INTO comments (message_id,user_id, comment, created_at, updated_at)
                VALUES (:message_id, :user_id, :comment, NOW(), NOW())'''
    print "line 109"
    data = {
            'user_id': session['user_id'],
            'message_id': message_id,
            'comment': request.form['comment']
    }
    print "line 114"
    mysql.query_db(query, data)
    return redirect ('/paulwall')

#delete post
@app.route('/post/<message_id>/delete', methods=['GET'])
def dpost(message_id):
    print "line 122"
    data = {'message_id': message_id}
    print message_id
    query = "DELETE FROM comments WHERE comments.message_id= :message_id"
    mysql.query_db(query, data)
    query = "DELETE FROM messages WHERE messages.id = :message_id"
    mysql.query_db(query, data)
    print "line 126"
    return redirect('/paulwall')

#delete comment
@app.route('/comment/<comment_id>/delete', methods=['GET'])
def dcomment(comment_id):
    print "line 157"
    print comment_id
    data = {'comment_id': comment_id}
    query = "DELETE FROM comments WHERE comments.id = :comment_id"
    mysql.query_db(query, data)
    print "line 162"
    return redirect('/paulwall')

#logout
@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    print "Logged Out"
    return redirect ('/')

app.run(debug=True)
