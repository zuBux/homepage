from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from app import db


class Post(db.Model):
  __tablename__ = 'post'
  id = db.Column(Integer, primary_key=True)
  title = db.Column(String(120))
  body = db.Column(Text)
  pub_date = db.Column(DateTime)

  def __init__(self, title, body, pub_date=None):
    self.title = title
    self.body = body
    if pub_date is None:
        pub_date = datetime.utcnow()
    self.pub_date = pub_date

  def __repr__(self):
    return '<Post %r>' % self.title


class Advisory(db.Model):
  __tablename__ = 'advisories'
  id = db.Column(Integer, primary_key=True)
  title = db.Column(String(180))
  summary = db.Column(Text)
  body = db.Column(Text)
  pub_date = db.Column(DateTime)

  def __init__(self, title, summary, body, pub_date=None):
    self.title = title
    self.body = body
    if pub_date is None:
        pub_date = datetime.utcnow()
    self.pub_date = pub_date
    self.category = category

  def __repr__(self):
    return '<Advisory %r>' % self.title