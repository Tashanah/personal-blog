from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,SelectField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title  = StringField('Review title',validators=[Required()])
    review = TextAreaField('Blog Review', validators=[Required()])
    submit = SubmitField('submit')

class UpdateBlog(FlaskForm):
    blog = TextAreaField('Edit your blog here', validators = [Required ()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField("Blog Title",validators=[Required()])
    blog = TextAreaField('Write your blog post here')
    submitted_by = TextAreaField('Write your name here')
    submit = SubmitField('Submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
