from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import BlogForm,UpdateBlog,ReviewForm,UpdateProfile
from ..import db,photos
from ..models import User,Blog,Quote,Review
from flask_login import login_required,current_user
from ..requests import get_quote
import markdown2
# import requests
# Review =reviews.Review 

@main.route("/")
def index():
    """
    View root page function that return the index page and its data
    """
    blogs = Blog.query.all()
    
    show_quote=get_quote()
    quote=show_quote["quote"]
    quote_author=show_quote["author"]
    title = "Home - Welcome to Blogger"
    return render_template('index.html',title=title, quote=quote,quote_author=quote_author,blogs = blogs)




@main.route("/details/<int:id>", methods=['GET', 'POST'])
@login_required
def details(id):

    reviews = Review.query.all()
    form = ReviewForm()
    if form.validate_on_submit():
        title = form.title.data
        review= form.review.data
        

        # Updated blog instance
        new_review = Review()
        new_review.title = title
        new_review.blog = review
        new_review.submit=submit
        # new_blog.author=current_user

        new_review.save_review()

        return redirect(url_for('main.details', id = id))
   
    blog=Blog.query.get_or_404(id)
    return render_template("new_review.html", blog=blog, form = form, reviews = reviews)


@main.route("/blog",methods=['GET','POST'])
@login_required
def blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        blog_post = form.blog.data
        submitted_by=form.submitted_by.data

        # Updated blog instance
        new_blog = Blog()
        new_blog.title = title
        new_blog.blog = blog_post
        new_blog.submitted_by=submitted_by
        new_blog.author=current_user

        # new_pitch = Pitch(pitch = pitch)

        # save pitch method
        new_blog.save_blog()

        return redirect(url_for('main.index'))

    title="Post your entry"
    return render_template('blog.html',title=title,form=form)


@main.route('/quote/<int:quote>')
def quotes(quote):

    '''
    View quotes page function that returns the quote details page and its data
    '''
    quote = get_quotes(quote)
    title = f'{quote.quote}'

    return render_template('quote.html',title = title,quote = quote)  


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

# @main.route('/review/<int:id>')
# def single_review(id):
#     review=Review.query.get(id)
#     if review is None:
#         abort(404)
#     format_review = markdown2.markdown(review.movie_review,extras=["code-friendly", "fenced-code-blocks"])
#     return render_template('review.html',review = review,format_review=format_review)