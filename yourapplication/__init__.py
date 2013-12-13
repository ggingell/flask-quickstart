__author__ = 'grantgingell'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_path='/Users/grantgingell/Documents', instance_relative_config=True)

import yourapplication.views

#db = SQLAlchemy(app)

#@app.errorhandler(404)
#def page_not_found(error):
#   return render_template('page_not_found.html'), 404
