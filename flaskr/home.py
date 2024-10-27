from flask import Blueprint , render_template

bp = Blueprint('home', __name__ , url_prefix='/' , template_folder='templates/home')

@bp.route('/')
def home():
    return render_template('index.html')