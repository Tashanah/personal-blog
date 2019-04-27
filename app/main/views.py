from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import BlogForm,UpdateBlog,ReviewForm
from ..import db,photos
from ..models import User,Blog,Quote,Review,
from flask_login import login_required,current_user
import markdown2

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

