__author__ = 'grantgingell'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_path='/Users/grantgingell/Documents', instance_relative_config=True)
app.config.from_pyfile('flask-quickstart-dev.cfg', silent=False) # Also below. TODO: May not be needed there?

import yourapplication.views

#db = SQLAlchemy(app)


#@app.errorhandler(404)
#def page_not_found(error):
#   return render_template('page_not_found.html'), 404

#if __name__ == '__main__':
    #app.config.from_pyfile('flask-quickstart-dev.cfg', silent=False)
    #app.run()