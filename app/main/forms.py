from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,SelectField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title  = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie Review', validators=[Required()])
    submit = SubmitField('submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators = [Required ()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField("Pitch Title",validators=[Required()])
    blog = TextAreaField('Write your blog post here')
    submitted_by = TextAreaField('Write your name here')
    submit = SubmitField('Submit')
    