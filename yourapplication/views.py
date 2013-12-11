__author__ = 'grantgingell'

from yourapplication import app
from flask import render_template


@app.route('/')
def index():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name=name)
