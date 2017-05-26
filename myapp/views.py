from myapp import app
from myapp.forms import LoginForm
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

@app.route('/login', methods=['GET','POST'])
def login():
	lForm = LoginForm()
	return render_template('login.html',title='Sign in',form=lForm)
