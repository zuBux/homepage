from flask import Flask, render_template, request, session, flash, redirect, url_for
from datetime import datetime
from database import db_session
from models import Post
from app import app
import hashlib

#app = Flask(__name__)
app.config.from_envvar('FLASK_SETTINGS')


@app.route('/')
def index():
  return render_template('index.html', nodict={})


@app.route('/blog')
def blog():
  posts = Post.query.order_by(-Post.pub_date)
  first = posts.first()
  older = posts[1:]
  return render_template('blog.html', first=first, posts=older)


@app.route('/blog/post/<post_id>')
def view_post(post_id):
  error = None
  try:
    post = Post.query.get(post_id)
    older = Post.query.filter(Post.id < post_id)[:3]
  except:
    print "No such post"
  return render_template('post.html', post=post, posts=older)


@app.route('/about')
def about():
  return render_template('about.html', nodict={})


# No user model in DB since we require only one user.No plaintext pass though
@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    hash_pass = hashlib.sha256(request.form['password']).hexdigest()
    print "got it"
    if request.form['username'] != app.config['USERNAME']:
        error = 'Invalid username'
    elif hash_pass != app.config['PASSWORD']:
        error = 'Invalid password'
    else:
        session['logged_in'] = True
        flash('You were logged in')
        return redirect(url_for('blog'))
  return render_template('login.html', error=error)
