import functools
from typing import Callable, TypeVar, Type

from weary.create_instance import create
from weary.property_definition import property

T = TypeVar("T")


def model(f: Callable[..., T]) -> Callable[..., T]:
    @functools.wraps(f)
    def wrapper(*args, **kw) -> T:
        return f(*args, **kw)

    return wrapper


