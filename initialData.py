#!/usr/bin/env python
from datetime import datetime
from myapp import db
from myapp.models import User, Post

u1 = User(nickname='John', email='john@email.com')
u2 = User(nickname='Susan', email='susan@email.com')
db.session.add(u1)
db.session.add(u2)

p1 = Post(body='My first post', timestamp=datetime.utcnow(), author=u1)
p2 = Post(body='My second post', timestamp=datetime.utcnow(), author=u1)
p3 = Post(body='The weather is hot', timestamp=datetime.utcnow(), author=u2)
p4 = Post(body='I need ice-cream', timestamp=datetime.utcnow(), author=u2)

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)

db.session.commit()
