#!/usr/bin/env python
from myapp import db
from myapp.models import User, Post

for p in Post.query.all():
	db.session.delete(p)

for u in User.query.all():
	db.session.delete(u)

db.session.commit()
