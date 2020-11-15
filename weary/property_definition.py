from typing import Callable, TypeVar

from weary.method_registrations import method_registrations

T = TypeVar("T")


def property(clazz, function_name) -> Callable[..., Callable[..., T]]:
    def wrapper_builder(f: Callable[..., T]) -> Callable[..., T]:
        if clazz not in method_registrations:
            method_registrations[clazz] = dict()

        method_registrations[clazz][function_name] = f
        return f

    return wrapper_builder
