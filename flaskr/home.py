from flask import Blueprint , render_template , redirect , url_for , request
from flaskr.auth import is_logged_in

bp = Blueprint('home', __name__ , url_prefix='/' , template_folder='templates/home')

@bp.route('/')
@is_logged_in
def home():
    return render_template('index.html')