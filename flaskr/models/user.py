import uuid
from datetime import datetime
from flaskr.utils.password import hash_password


class User:
    def __init__(self, name, email, password):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password = hash_password(password)
        self.created_at = datetime.now().isoformat()
