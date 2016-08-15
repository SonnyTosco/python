from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'very secret'

@app.route('/')
def index():
  return render_template('index.html')
@app.route('/create', methods=['POST'])
def create():
    print "test"
    data = request.form
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
    elif len(request.form['comments']) > 120:
        flash("You talk too much. Shorten your comment")
    elif len(request.form['name']) > 1:
        flash("Success! Your name is {}".format(request.form['name']))
    print data
    return render_template('result.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
