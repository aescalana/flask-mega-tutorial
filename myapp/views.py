from myapp import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	mockUser = {'nickname':'Manuel'}
	mockPosts = [
		{
			'author': {'nickname':'John'},
			'body': 'Beautiful day in Portland'
		},
		{
			'author': {'nickname':'Susan'},
			'body': 'The Avengers movie was so cool'
		}
	]
	return render_template('index.html',title='Home',user=mockUser, posts=mockPosts)
