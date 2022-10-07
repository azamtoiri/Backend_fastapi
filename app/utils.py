from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # hashing algorithm


def hash(password: str) -> str:
    return pwd_context.hash(password)


def re_hash(password: str) -> str:
    return pwd_context.encrypt(password)
