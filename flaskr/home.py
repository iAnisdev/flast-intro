from flask import Blueprint , render_template , session , request
from .auth import is_logged_in
from flaskr.utils.token import decode_token
from datetime import datetime
import json 

bp = Blueprint('home', __name__ , url_prefix='/' , template_folder='templates/home')
file_path = 'flaskr/data/todo.json'

@bp.route('/' , methods=['GET'])
@is_logged_in
def home():
     if request.method == 'GET':
        with open(file_path, 'r') as todos_file:
            try:
                data = json.load(todos_file)
            except json.JSONDecodeError:
                data = {}
            if 'todos' not in data:
                return render_template('index.html' , todos=[])
            user = decode_token(session['token'])
            user_todos = [todo for todo in data['todos'] if todo['user_id'] == user['id']]
            for todo in user_todos:
                todo["formatted_date"] = datetime.fromisoformat(todo["created_at"]).strftime("%B %d, %Y, %I:%M %p")
            return render_template('index.html' , todos=user_todos)