from typing import Optional, cast

from decouple import config


def _str_config(search_path: str, *args, **kwargs) -> str:
    obj = config(search_path, *args, **kwargs)
    return cast(str, obj)


class Connection:
    DATABASE_URL = _str_config("DATABASE_URL")
