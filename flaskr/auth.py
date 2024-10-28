from flask import Blueprint , render_template , redirect , url_for , request , flash , session
from flaskr.models.user import User
from flaskr.utils.password import verify_password
from flaskr.utils.token import encode_token

import json

bp = Blueprint('auth', __name__ , url_prefix='/auth' , template_folder='templates/auth')
file_path = 'flaskr/data/users.json'

def is_logged_in(view):
    def wrapped_view(**kwargs):
        if 'token' in session:
            return view(**kwargs)
        else:
            return redirect(url_for('auth.login'))
    return wrapped_view

def is_not_logged_in(view):
    def wrapped_view(**kwargs):
        if 'token' not in session:
            return view(**kwargs)
        else:
            return redirect('/')
    return wrapped_view

@bp.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        with open(file_path, 'r') as users_file:
            try:
                data = json.load(users_file)
            except json.JSONDecodeError:
                data = {}
        if 'users' not in data:
            flash('User not found' , "danger")
            return redirect(url_for('auth.login'))
        for user in data['users']:
            if user['email'] == email:
                if verify_password(user['password'] , password):
                    token = encode_token({'id': user['id']})
                    session.clear()
                    session['token'] = token
                    flash('Welcome to Todo App!' , "success")
                    return redirect('/')
                else:
                    flash('Invalid password' , "danger")
                    return redirect(url_for('auth.login'))
            else:
                flash('User not found' , "danger")
                return redirect(url_for('auth.login'))
    else:
        if 'token' in session:
            return redirect('/')
        return render_template('login.html')

@bp.route('/register' , methods=['GET' , 'POST'])
def register():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            new_user = User(name , email , password)
            with open(file_path, 'r') as users_file:
                try:
                    data = json.load(users_file)
                except json.JSONDecodeError:
                    data = {}
            if 'users' not in data:
                data['users'] = []
            for user in data['users']:
                if user['email'] == email:
                    flash('Email already registered' , "danger")
                    return redirect(url_for('auth.register'))
            data['users'].append(new_user.__dict__)
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            flash('User registered successfully' , "success")
            return redirect(url_for('auth.login'))
        except Exception as e:
             flash('Error: ' + str(e) , "danger")
             return redirect(url_for('auth.register'))
    else:
        if 'token' in session:
            return redirect('/')
        return render_template('register.html')

@bp.route('/logout' , methods=['POST'])
@is_logged_in
def logout():
    session.clear()
    flash('User logged out successfully' , "success")
    return redirect(url_for('auth.login'))

@bp.route('/')
def redirect_route():
    return redirect(url_for('auth.login'))
