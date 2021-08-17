import functools
from typing import Callable

_property = property


def property(fn: Callable):
    @_property
    @functools.wraps(fn)
    def not_implemented_wrapper(*args, **kw):
        raise NotImplementedError(f"The property definition wasn't implemented for {fn}")

    return not_implemented_wrapper
