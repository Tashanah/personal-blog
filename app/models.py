from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Blog(db.Model):
    '''
    Blog class to define the blog objects
    '''
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    blog = db.Column(db.String)
    submitted_by = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
  
    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls, id):
        blogs = Blog.query.filter_by(blog_id=id).all()
        return blogs 

class Quote:
    '''
    Quotes class to define random quote objects from the API
    '''

    def __init__(self,id,author,quote):
        self.id =id
        self.author = author
        self.quote = quote
        
class Review(db.Model):
    '''
    review class to allow users to comment on a blog post
    '''
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    blog = db.Column(db.String)
    submitted_by = db.Column(db.String)
    Review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_review(self):
        Review.all_reviews.append(self)
        db.session.add(self)
        db.session(commit)
    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls, blog):

        response = []

        for review in cls.all_reviews:
            if review.pitch == blog:
                response.append(review)

        return response

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")
    # pitches=db.relationship('Pitch', backref='user', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # def save_user(self):
    #     db.session.add(self)
    #     db.session.commit()

    def __repr__(self):
        return f'User {self.username}'




