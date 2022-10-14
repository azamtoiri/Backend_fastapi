from typing import cast
from decouple import config


def _str_config(searching_path: str, *args, **kwargs) -> str:
    """Convert to string"""
    obj = config(searching_path, *args, **kwargs)

    return cast(str, obj)


def _int_config(searching_path: int, *args, **kwargs) -> int:
    obj = config(searching_path, *args, **kwargs)

    return int(obj)


class Connection:
    """Config connection to database"""

    DATABASE_URL = _str_config("DATABASE_URL")


class Server:
    """Config related to the API server itself"""

    SECRET_KEY = _str_config("SECRET_KEY")
    ALGORITHM = _str_config("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = _int_config("ACCESS_TOKEN_EXPIRE_MINUTES")
