from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Optional
from wtforms.widgets import TextArea

class JobPostForm(FlaskForm):
    poster_email = StringField('Your email for us to contact you',
                               validators=[DataRequired(), Email()])
    title = StringField('Title of Job Posting', validators=[DataRequired()])
    body = TextAreaField('Job posting content', validators=[DataRequired()],
                    widget=TextArea())
    apply_here_email = StringField('Email applicant can use to apply/inquire',
                                   validators=[DataRequired(), Email()])
    link_to_application_site = StringField('Link to your application site if applicable (optional)',
                                           validators=[Optional()])
    job_location = StringField('Job location(s)', validators=[DataRequired()])
    org_name = StringField('Organization or Company name',
                                    validators=[DataRequired()])
    submit = SubmitField('Submit job posting')
