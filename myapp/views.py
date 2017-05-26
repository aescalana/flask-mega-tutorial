from myapp import app
from myapp.forms import LoginForm
from flask import render_template, flash, redirect

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
	if lForm.validate_on_submit():
		flash('Login requested for OpenID=%s, remember_me=%s' % (lForm.openid.data,str(lForm.remember_me.data)))
		return redirect('/index')
	else:
		return render_template('login.html',title='Sign in',form=lForm,providers=app.config['OPENID_PROVIDERS'])
