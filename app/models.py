from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from app import db

class Post(db.Model):
  __tablename__ = 'post'
  id = db.Column(Integer, primary_key=True)
  title = db.Column(String(120))
  summary = db.Column(Text)
  body = db.Column(Text)
  pub_date = db.Column(DateTime)

  category_id = db.Column(Integer, ForeignKey('category.id'))
  category = relationship('Category',
        backref=backref('posts', lazy='dynamic'))

  def __init__(self, title, body, category, pub_date=None):
    self.title = title
    self.body = body
    if pub_date is None:
        pub_date = datetime.utcnow()
    self.pub_date = pub_date
    self.category = category

  def __repr__(self):
    return '<Post %r>' % self.title

class Category(db.Model):
  __tablename__ = 'category'
  id = db.Column(Integer, primary_key=True)
  name = db.Column(String(80))
  description = Column(Text)

  def __init__(self, name, descr):
    self.name = name
    self.description = descr
  def __repr__(self):
    return '<Category %r>' % self.name
