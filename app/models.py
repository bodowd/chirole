from datetime import datetime
from app import db

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poster_email = db.Column(db.String(120), unique=False)
    date_posted = db.Column(db.Date, index=True, unique=False)
    body = db.Column(db.Text)
    title = db.Column(db.String(140))
    apply_here_email = db.Column(db.String(120), unique=False)
    link_to_application_site = db.Column(db.String(100), unique=False)
    job_location = db.Column(db.String(120), unique=False)
    org_name = db.Column(db.String(120), unique=False)

    def __repr__(self):
        return f'<Poster email: {self.poster_email},\
                Date posted: {self.date_posted},\
                title: {self.title},\
                Apply Here email: {self.apply_here_email}>'
