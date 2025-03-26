import jwt
from datetime import datetime, timedelta
from config import SECRET_KEY, UTC, WIB

def create_jwt(username):
    now = datetime.now(UTC)
    payload = {
        "username": username,
        "iat": now,
        "exp": now + timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verify_jwt(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        return "Token has expired"
    except jwt.InvalidTokenError:
        return "Invalid token"
