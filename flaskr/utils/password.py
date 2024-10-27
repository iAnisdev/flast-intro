import hashlib
import secrets

def hash_password( password):
    salt = secrets.token_hex(16)
    hashed_password = hashlib.sha256((salt + password).encode() + password.encode()).hexdigest()
    return f"{salt}${hashed_password}"

def verify_password( hashed_password, password):
    salt, hashed = hashed_password.split('$')
    return hashed == hashlib.sha256((salt + password).encode() + password.encode()).hexdigest()