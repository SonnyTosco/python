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
    return redirect('/')
@app.route('/ninja', methods=['POST'])
def ninja():
    print "all good"
    if session.get('counter')==None:
        session['counter']=0
    session['counter']=session['counter']+1
    return redirect('/')
@app.route('/zero', methods=['POST'])
def zero():
    print "all good"
    session['counter']=0
    return redirect('/')
app.run(debug=True)
