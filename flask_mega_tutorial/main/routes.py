from flask import Blueprint, render_template

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
@main_bp.route('/home')
def home():
    user = {'username': 'Joe'}
    posts = [
        {'body': 'Python is fun!', 'author': {'username': 'Shane'}},
        {'body': 'Python for president!', 'author': {'username': 'Chris'}},
    ]
    return render_template('home.html', title="Home", user=user, posts=posts)

