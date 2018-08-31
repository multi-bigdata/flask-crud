import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    comments = db.relationship("Comment", backref='post')
    
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.datetime.now()

# CREATE TABLE posts(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR,
#     content TEXT,
#     created_at DATETIME
# )
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    create_at = db.Column(db.DateTime)
    # FK
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    
    def __init__(self, content):
        self.content = content
        self.create_at = datetime.datetime.now()