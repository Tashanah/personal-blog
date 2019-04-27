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
    Blog class to define the blogs
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
