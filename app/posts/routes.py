from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from app.models import Posts
from app import db
from app.posts.forms import JobPostForm, DeleteJobForm

posts = Blueprint('posts', __name__)

@posts.route('/post_job', methods=['GET','POST'])
def post_job():
    form = JobPostForm()
    if form.validate_on_submit():
        title = form.title.data
        poster_email = form.poster_email.data
        body = form.body.data
        apply_here_email = form.apply_here_email.data
        job_location = form.job_location.data
        org_name = form.org_name.data
        link_to_application_site = form.link_to_application_site.data
        # a datetime object -- DB has a Date object. Will only accept
        # python datetime objects
        date_posted = datetime.today()

        post_to_db = Posts(title=title, poster_email=poster_email, body=body,
                           apply_here_email=apply_here_email,
                           job_location=job_location,
                           date_posted=date_posted,
                           link_to_application_site=link_to_application_site,
                           org_name=org_name)

        db.session.add(post_to_db)
        db.session.commit()
        flash('Your job posting has been submitted!', 'success')
        return redirect(url_for('main.home'))
    return render_template('post_job.html', title='Post a job', form=form)

@posts.route('/edit_job/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_job(post_id):
    form = JobPostForm()
    if form.validate_on_submit():
        print('Valid on submission')
        # get the existing post
        job_post = Posts.query.get_or_404(post_id)

        # get the data from the form
        job_post.title = form.title.data
        job_post.poster_email = form.poster_email.data
        job_post.body = form.body.data
        job_post.apply_here_email = form.apply_here_email.data
        job_post.job_location = form.job_location.data
        job_post.org_name = form.org_name.data
        job_post.link_to_application_site = form.link_to_application_site.data

        db.session.commit()
        flash('The job post has been updated!', 'success')
        return redirect(url_for('posts.view_job', post_id=job_post.id))

    elif request.method == 'GET':
        print('Getting form...')
        # prepopulate the form
        job_post = Posts.query.get_or_404(post_id)

        form.body.data = job_post.body
        form.title.data = job_post.title
        form.poster_email.data = job_post.poster_email
        form.apply_here_email.data = job_post.apply_here_email
        form.job_location.data = job_post.job_location
        form.org_name.data = job_post.org_name
        form.link_to_application_site.data = job_post.link_to_application_site

    return render_template('post_job.html', title='Edit job posting', form=form)


@posts.route('/view_job/<int:post_id>', methods=['GET', 'POST'])
def view_job(post_id):
    job_post = Posts.query.get_or_404(post_id)
    return render_template('view_job.html', job_post=job_post)

@posts.route('/delete_job/<int:post_id>', methods=['GET','POST'])
@login_required
def delete_job(post_id):
    form = DeleteJobForm()
    job_post = Posts.query.get_or_404(post_id)
    print(form.accept, form.delete)
    if form.validate_on_submit():
        print('valid')
        Posts.query.filter_by(id=post_id).delete()
        db.session.commit()
        flash('Post deleted', 'success')
        return redirect(url_for('main.home'))


    return render_template('delete_job.html', job_post=job_post, form=form)
