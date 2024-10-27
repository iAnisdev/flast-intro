import jwt
import uuid

secret = str(uuid.uuid4())

def encode_token(data):
    return jwt.encode(data,secret, algorithm="HS256")

def decode_token(token):
    return jwt.decode(token, secret, algorithms=["HS256"])