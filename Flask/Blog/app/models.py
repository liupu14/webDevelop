from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    img = db.Column(db.String(60),nullable=False,default="./static/images/placeholder.png")
    password = db.Column(db.String(60),unique=False,nullable=False)
    post = db.relationship("Post",backref="author",lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.img}')"


class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),unique=False,nullable=False)
    post_date = db.Column(db.Date,nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.post_date}')"