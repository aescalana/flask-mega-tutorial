#!/usr/bin/env python
from myapp import db
from myapp.models import User, Post

print 'USER'
users = User.query.all()
for u in users:
	print '%d, %s, %s' % (u.id,u.email,u.nickname)

print 'POST'
posts = Post.query.all()
for p in posts:
	print '%d: %s' % (p.id, p.body)

id = 1
u = User.query.get(id)
if u:
	print 'GET %d' % id
	print 'User %d is %s' % (u.id, u.nickname)

	for p in u.posts:
		print '%s: %s' % (p.timestamp, p.body)
