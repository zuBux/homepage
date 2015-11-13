from flask import Flask, render_template, request, session, flash, redirect, url_for
from datetime import datetime
#from database import db_session
from models import Post
from forms import PostForm, LoginForm
from app import app, db
import hashlib

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


@app.route('/blog/post/add', methods=['GET', 'POST'])
def add_post():
  if session['logged_in'] is not True:
    return render_template("unauthorized.html", dict={})
  form = PostForm()
  if request.method == 'POST':
    title = request.form['title']
    body = request.form['body']
    new_post = Post(title, body)
    db.session.add(new_post)
    db.session.commit()
  return render_template("edit.html", action="Add", form=form)


@app.route('/blog/post/<post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
  if session['logged_in'] is not True:
    return render_template("unauthorized.html", dict={})
  post = Post.query.get(post_id)
  form = PostForm(obj=post)
  if request.method == 'POST':
    post.title = request.form['title']
    post.body = request.form['body']
    db.session.add(post)
    db.session.commit()
  return render_template("edit.html", action="Add", form=form)


@app.route('/about')
def about():
  return render_template('about.html', nodict={})


# No user model in DB since we require only one user.No plaintext pass though
@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
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
  return render_template('login.html', error=error, form=form)


@app.route('/logout')
def logout():
  session['logged_in'] = False
  return redirect(url_for('index'))