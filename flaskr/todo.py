from flask import Blueprint , render_template , session, request, redirect, flash
from .auth import is_logged_in
from flaskr.utils.token import decode_token
from flaskr.models.todo import Todo
import json


bp = Blueprint('todo', __name__ , url_prefix='/todo', template_folder='templates/todo')
file_path = 'flaskr/data/todo.json'

@bp.route('/add', methods=['GET' , 'POST'])
@is_logged_in
def add():
    if request.method == 'POST':
        title = request.form['title']
        user_id = decode_token(session['token']).get('id')
        todo = Todo(user_id , title)
        with open(file_path, 'r') as todo_file:
            try:
                data = json.load(todo_file)
            except json.JSONDecodeError:
                data = {}
        if 'todos' not in data:
            data['todos'] = []
        data['todos'].append(todo.__dict__)
        with open(file_path, 'w') as todo_file:
            json.dump(data, todo_file, indent=4)
            flash('Todo added successfully' , "success")
            return redirect('/')
    else:
        return render_template('todo.html', mode='add')