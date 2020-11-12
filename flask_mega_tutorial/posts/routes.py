from flask import Blueprint, abort, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from flask_mega_tutorial import db
from flask_mega_tutorial.models import Post
from flask_mega_tutorial.posts.forms import PostForm

posts_bp = Blueprint('posts_bp', __name__)

@posts_bp.route('/post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        redirect(url_for('main_bp.home'))
    return render_template('create_post.html', form=form)

@posts_bp.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('view_post.html', post=post)

@posts_bp.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if request.method == 'GET':
        form.body.data = post.body
    elif form.validate_on_submit():
        post.body = form.body.data
        db.session.commit()
        return redirect(url_for('posts_bp.post', post_id=post.id))
    return render_template('create_post.html', form=form)
