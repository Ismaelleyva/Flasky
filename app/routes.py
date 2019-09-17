from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/secret')
def secret():
    return "you found the secret"

@app.route('/apple')
def apple():
    return "there is an apple"
@app.route('/appledrama')
def appledrama():
    return "there is no apple"

@app.route('/results', methods = ["GET", "POST"])
def results():
    return "this is the results page"
    userdata = dict(request.form)
    print(userdata)
    print(userdata,['nickname'])
    nickname = userdata['nickname']
    print(nickname)
    output= model.shout(userdata['nickname'])
    print(output)
    return render_template('results.html')
