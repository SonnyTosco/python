from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    print "g2g"
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def process():
    print "Gucci"
    data=request.form
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
    else:
        flash("Success! Your name is {}".format(request.form['name']))
    return redirect('/', data=data) # either way the application should return to the index and display the message
app.run(debug=True)
