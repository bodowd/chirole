from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Optional, URL
from wtforms.widgets import TextArea

class JobPostForm(FlaskForm):
    poster_email = StringField('Your email for us to contact you*',
                               validators=[DataRequired(), Email()])
    title = StringField('Title of Job Posting*', validators=[DataRequired()])
    body = TextAreaField('Job posting content*', validators=[DataRequired()],
                    widget=TextArea())
    apply_here_email = StringField('Email that applicant can use to apply/inquire (if applicable)',
                                   validators=[Email(), Optional()])
    link_to_application_site = StringField('Link to your application site (if applicable) \
        please make sure it starts with `http://www` i.e. http://www.yourwebsite.com',
                                           validators=[Optional(), URL()])
    job_location = StringField('Job location(s)*', validators=[DataRequired()])
    org_name = StringField('Organization or Company name*',
                                    validators=[DataRequired()])
    accept = BooleanField('I have reviewed my job posting and would like to \
         submit it for posting for 30 days from time of payment.*',
          validators=[DataRequired()])
    submit = SubmitField('Submit job posting')

class DeleteJobForm(FlaskForm):
    accept = BooleanField('Delete the post?', validators=[DataRequired()])
    delete = SubmitField('Delete job posting')
