from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'very secret'

@app.route('/')
def index():
    print "g2g"
    if session.get('counter')==None:
        session['counter']=0
    session['counter']=session['counter']+1
    return render_template('index.html')
# def counter():
#     print "g2g2"
#     counter=request.form['counter']
#     return render_template('index.html', counter='1')
app.run(debug=True)
