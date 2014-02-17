__author__ = 'grantgingell'

from yourapplication import app
app.config.from_pyfile('flask-quickstart-dev.cfg', silent=True)
app.run()
