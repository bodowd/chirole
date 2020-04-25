from flask import Blueprint, render_template
from flask_login import current_user
from app.models import Posts
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def home():

    posts = Posts.query.order_by(Posts.id.desc()).all()
    print(posts)

    # not optimal. Should filter in the database query
    posts_for_display = []
    for p in posts:
        today = datetime.today().strftime('%Y-%m-%d')
        p_date = p.date_posted.strftime('%Y-%m-%d')
        p.date_str = p_date
        days_since = (datetime.strptime(today, '%Y-%m-%d') -\
             datetime.strptime(p_date, '%Y-%m-%d')).days
        if days_since == 0:
            p.days_since_post = 'Today'
        elif days_since == 1:
            p.days_since_post = f'{days_since} day ago'
        else:
            p.days_since_post = f'{days_since} days ago'

        # not optimal. Should filter in the database query
        if days_since <= 30 and p.paid:
            posts_for_display.append(p)

    # make it so you cannot view home page if logged in
    # so that you don't forget to logout
    if current_user.is_authenticated:
        return render_template('logged_in.html', posts=posts_for_display)

    # reverse so that the newest posts are shown at the top of the list
    return render_template('home.html', posts=posts_for_display)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/tos')
def tos():
    return render_template('tos.html')

@main.route('/privacy')
def privacy():
    return render_template('privacy.html')
