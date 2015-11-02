from flask import Flask
from flask import render_template
from datetime import datetime
from database import db_session
from models import Post

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', nodict = {})

@app.route('/blog')
def blog():
  posts = Post.query.order_by(-Post.pub_date)
  first = posts.first()
  older = posts[1:]
  return render_template('blog.html',first=first, posts=older)

@app.route('/about')
def about():
  return render_template('about.html', nodict= {})

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
