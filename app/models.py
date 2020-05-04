from datetime import datetime
from app import db
from config import Config
from flask_login import UserMixin
from app import db, login_manager

class Posts(db.Model):
    # __tablename__ = 'posts' # commented out makes it work with flask db upgrade on the linux server...?

    id = db.Column(db.Integer, primary_key=True)
    poster_email = db.Column(db.String(120), unique=False)
    date_posted = db.Column(db.Date, index=True, unique=False)
    body = db.Column(db.Text)
    title = db.Column(db.String(140))
    apply_here_email = db.Column(db.String(120), unique=False)
    link_to_application_site = db.Column(db.String(200), unique=False)
    job_location = db.Column(db.String(120), unique=False)
    org_name = db.Column(db.String(120), unique=False)
    paid = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Poster email: {self.poster_email},\
                Date posted: {self.date_posted},\
                title: {self.title},\
                Apply Here email: {self.apply_here_email}>'


class User(UserMixin):
    pass


credentials = {'username': Config.APP_USERNAME,
               'password': Config.APP_PASSWORD}


# # decorator lets login_manager package find the user in the session
@login_manager.user_loader
def load_user(username):
    if username != credentials['username']:
        return None
    user = User()  # UserMixin class contains methods needed by flask-login
    return user
