from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import BlogForm,UpdateBlog,ReviewForm
from ..import db,photos
from ..models import User,Blog,Quote,Review
from flask_login import login_required,current_user
from ..requests import get_quotes,process_results
import markdown2
# Review =reviews.Review 

@main.route("/")
def index():
    """
    View root page function that return the index page and its data
    """
    blogs = blog.query.all()

    title = "Home - Welcome to Blogger"
    return render_template('index.html',title=title,blogs=blogs)


@main.route("/blog",methods=['GET','POST'])
@login_required
def blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        blog_post = form.blog_post.data
        

        # Updated blog instance
        new_blog = blog()
        new_blog.title = title
        new_blog.blog_post = blog_post
        

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

@main.route('/blog/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    blog = get_blog(title)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(id,blog,submitted_by)
        new_review.save_review()
        return redirect(url_for('blog',id = id ))

    title = f'{blog.title} review'
    return render_template('new_review.html',title = title, review_form=form, blog=blog)

@main.route('/blog/<int:id>')
def blog(id):

    '''
    View blog page function that returns the blog details page and its data
    '''
    blog = get_blog(id)
    title = f'{blog.title}'
    reviews = Review.get_reviews(blog.id)

    return render_template('blog.html',title = title,blog=blog,reviews = reviews)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)