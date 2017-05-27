from myapp import app, db, lm, oid
from myapp.forms import LoginForm
from myapp.models import User
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required

@app.before_request
def before_request():
	g.user = current_user

@app.route('/')
@app.route('/index')
@login_required
def index():
	user = g.user
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
	return render_template('index.html',title='Home', user=user, posts=mockPosts)

@app.route('/login', methods=['GET','POST'])
@oid.loginhandler
def login():
	if g.user and g.user.is_authenticated:
		# The url_for takes the name of the function as parameter
		return redirect(url_for('index'))
	lForm = LoginForm()
	if lForm.validate_on_submit():
		session['remember_me'] = lForm.remember_me.data
		# Let OpenID authenticate the user elsewhere
		return oid.try_login(lForm.openid.data, ask_for=['nickname', 'email'])
	else:
		return render_template('login.html',title='Sign in',form=lForm,providers=app.config['OPENID_PROVIDERS'])

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@oid.after_login
def after_login(resp):
	# An empty string is falsy
	if resp.email:
		user = User.query.filter_by(email=resp.email).first()
		if user is None:
			nickname = resp.nickname if resp.nickname else resp.email.split('@')[0]
			user = User(nickname=nickname, email=resp.email)
			db.session.add(user)
			db.session.commit()
		remember_me = session['remember_me'] if 'remember_me' in session else False
		# Add None default value (in case remember_me was not in session)
		session.pop('remember_me',None)
		# Register valid login for user
		login_user(user, remember=remember_me)
		nextUrl = request.args.get('next')
		if not nextUrl:
			nextUrl = url_for('index')
		return redirect(nextUrl)
	else:
		flash('Invalid login. Please try again.')
		return redirect(url_for('login'))
