from flask import Blueprint , render_template , redirect , url_for , request

bp = Blueprint('auth', __name__ , url_prefix='/auth' , template_folder='templates/auth')

@bp.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return 'Login'

@bp.route('/register' , methods=['GET' , 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        return 'Register'

@bp.route('/logout' , methods=['POST'])
def logout():
    return 'Logout'

@bp.route('/')
def redirect_route():
    return redirect(url_for('auth.login'))
