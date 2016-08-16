from flask import Flask, redirect, render_template, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    displayAll = True
    return render_template('ninja.html', displayAll=displayAll)

@app.route('/ninja/<color>')
def getColor(color):
    displayAll = False
    return render_template('ninja.html', color=color, displayAll=displayAll)

app.run(debug=True)

# from flask import Flask, render_template, request, redirect
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     print "turtle power"
#     return render_template('index.html')
# @app.route('/ninja/<color>')
# def color(color):
#     print "april"
#     return render_template("ninja.html", username=username)
# @app.route('/ninja')
# def ninja()
# app.run(debug=True)
#
#Code I wrote is above. James' solution used for the server.py file
