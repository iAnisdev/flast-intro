import uuid
from datetime import datetime

class Todo:
    def __init__(self, user_id , title):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.title = title
        self.user_id = user_id
        self.completed = False
