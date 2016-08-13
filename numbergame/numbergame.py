from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'very secret'

@app.route('/')
def index():
    print "g2g"
    return render_template('index.html')
@app.route('/enter', methods=['POST'])
def ninja():
    print "all good"
    return redirect('/')
@app.route('/fail', methods=['POST'])
def ninja():
    print "fail good"
    if session.get('counter')==None:
        session['counter']=0
    session['counter']=session['counter']+1
    return redirect('/')
@app.route('/win', methods=['POST'])
def ninja():
    print "win good"
    if session.get('counter')==None:
        session['counter']=0
    session['counter']=session['counter']+1
    return redirect('/')
app.run(debug=True)
