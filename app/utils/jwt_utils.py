from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # hashing algorithm


def hash_(password: str) -> str:
    return pwd_context.hash(password)


def veryfi(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
