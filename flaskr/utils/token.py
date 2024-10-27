import jwt
import secrets

secret = secrets.token_hex()

def encode_token(data):
    return jwt.encode(data,secret, algorithm="HS256")

def decode_token(token):
    return jwt.decode(token, secret, algorithms=["HS256"])