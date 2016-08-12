from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'very secret'

@app.route('/')
def index():
    return render_template('new.html')
@app.route('/create', methods = ['POST'])
def create():
    d = request.form
    print d
    return render_template('show.html', data=d)
if __name__ == "__main__":
    app.run(debug=True)
