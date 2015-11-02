from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from database import Base
from datetime import datetime

class Post(Base):
  __tablename__ = 'post'
  id = Column(Integer, primary_key=True)
  title = Column(String(120))
  summary = Column(Text)
  body = Column(Text)
  pub_date = Column(DateTime)

  category_id = Column(Integer, ForeignKey('category.id'))
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

class Category(Base):
  __tablename__ = 'category'
  id = Column(Integer, primary_key=True)
  name = Column(String(80))
  description = Column(Text)

  def __init__(self, name, descr):
    self.name = name
    self.description = descr
  def __repr__(self):
    return '<Category %r>' % self.name
