from flask import Blueprint , render_template , session
from .auth import is_logged_in

bp = Blueprint('home', __name__ , url_prefix='/' , template_folder='templates/home')

@bp.route('/')
@is_logged_in
def home():
    print('Home')
    print(session['token'])
    return render_template('index.html')