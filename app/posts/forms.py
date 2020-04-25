from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Optional, URL, Length
from wtforms.widgets import TextArea

class JobPostForm(FlaskForm):
    poster_email = StringField('Your email for us to contact you*',
                               validators=[DataRequired(), Email(), Length(max=120)])
    title = StringField('Title of Job Posting*', validators=[DataRequired(), Length(max=140)])
    body = TextAreaField('Job description*', validators=[DataRequired()],
                    widget=TextArea())
    apply_here_email = StringField('Email that applicant can use to apply/inquire (if applicable)',
                                   validators=[Email(), Optional(), Length(max=120)])
    link_to_application_site = StringField('Link to your application site (if applicable) \
        Needs to include `http://www` i.e. http://www.yourwebsite.com',
                                           validators=[Optional(), URL(), Length(max=100)])
    job_location = StringField('Job location(s)*', validators=[DataRequired(), Length(max=120)])
    org_name = StringField('Organization or Company name*',
                                    validators=[DataRequired(), Length(max=120)])
    accept = BooleanField('I agree to the terms of service and privacy policy.*',
          validators=[DataRequired()])
    submit = SubmitField('Submit job posting and go to payment')

class DeleteJobForm(FlaskForm):
    accept = BooleanField('Delete the post?', validators=[DataRequired()])
    delete = SubmitField('Delete job posting')
