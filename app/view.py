from flask import Blueprint
from model import Post, User
from flask import render_template
from flask_login import current_user

bp = Blueprint('blog', __name__)


@bp.route('/')
@bp.route('/<int:page>')
def index(page=1):
    paginator = Post.objects.paginate(page=page, per_page=5)
    return render_template("index.html", paginator=paginator, user=current_user)


@bp.route('/posts/<string:post_id>')
def get_post(post_id):
    post = Post.objects(id=post_id).first()
    return render_template('post.html', post=post)


@bp.route('/about')
def about():
    user = User.objects.first()
    return render_template('about.html', user=user)
