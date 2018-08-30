# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import *


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///app'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    posts = Post.query.all()
    # SELECT * FROM posts;
    return render_template("index.html", posts=posts)
    
@app.route("/posts/new")
def new():
    return render_template("new.html")

@app.route("/post", methods=["POST"])
def create():
    # 사용자로부터 값을 가져와서 
    title = request.form.get('title')
    content = request.form.get('content')
    # DB에 저장
    post = Post(title=title, content=content)
    db.session.add(post)
    # INSERT INTO posts (title, content)
    # VALUES ('1번글', '1번내용');
    db.session.commit()
    return render_template("create.html", post=post)

@app.route("/posts/<int:id>")
def read(id):
    # DB에서 특정한 게시글(id)을 가져와!
    post = Post.query.get(id)
    # SELECT * FROM posts WHERE id=1;
    return render_template("read.html", post=post)
    
@app.route("/posts/<int:id>/delete")
def delete(id):
    # DB에서 특정 게시글 가져오기
    post = Post.query.get(id)
    # post 오브젝트 삭제하기
    db.session.delete(post)
    db.session.commit()
    # DELETE FROM posts WHERE id=2;
    return redirect('/')

@app.route("/posts/<int:id>/edit")
def edit(id):
    post = Post.query.get(id)
    return render_template("edit.html", post=post)


@app.route("/posts/<int:id>/update", methods=["POST"])
def update(id):
    post = Post.query.get(id)
    post.title = request.form.get("title")
    post.content = request.form.get("content")
    db.session.commit()
    return redirect("/posts/{}".format(post.id))
    # UPDATE posts SET title = "hihi"
    # WHERE id = 2;