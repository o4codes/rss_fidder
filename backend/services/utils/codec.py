from passlib.context import CryptContext
from jose import jwt, JWTError


class PasswordCodec:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash(self, password):
        return self.pwd_context.hash(password)

    def verify(self, password, hashed_password):
        return self.pwd_context.verify(password, hashed_password)

class TokenCodec:
    def __init__(self):
        pass