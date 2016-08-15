import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'very secret'

@app.route('/')
def index():
    if session.get('gold')==None:
        session['gold']=0
    print "golden"
    return render_template('index.html')
@app.route('/process_money', methods=['POST'])
def money():
    print "test"
    if request.form['building']=='farm':
        session['farm']=random.randrange(9,21)
        session['gold']+=session['farm']
    elif request.form['building']=='cave':
        session['cave']=random.randrange(4,11)
        session['gold']+=session['cave']
    elif request.form['building']=='house':
        session['house']=random.randrange(1,6)
        session['gold']+=session['house']
    elif request.form['building']=='casino':
        session['casino']=random.randrange(-51,51)
        session['gold']+=session['casino']
    print "swaggy"
    return redirect('/')
app.run(debug=True)
