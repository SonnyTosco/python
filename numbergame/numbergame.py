import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'very secret'

@app.route('/')
def index():
    if session.get('number')==None:
        session['number']=random.randrange(0,101)
        session['guess'] = None
    print session['number']
    return render_template('index.html')
@app.route('/enter', methods=['POST'])
def enter():
    print "enter"
    session['guess'] = request.form['guess']
    return redirect('/')
@app.route('/reset', methods=['GET'])
def reset():
    session.clear()
    return redirect('/')
app.run(debug=True)
