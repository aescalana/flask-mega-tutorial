from myapp import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	mockUser = {'nickname':'Manuel'}
	return render_template('index.html',user=mockUser)
