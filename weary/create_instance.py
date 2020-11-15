from typing import TypeVar, Type, Callable

from weary.method_registrations import method_registrations

T = TypeVar("T")

class WearyContext:
    def __init__(self) -> None:
        pass


def create(t: Type[T]) -> T:
    """
    Create the instance with the given type
    :param t:
    :return:
    """
    result = t()

    for method_name, method_impl in method_registrations[t].items():
        setattr(result, method_name, _context_provider(result, method_impl))

    return result


def _context_provider(this, method_impl: Callable) -> Callable:
    def result():
        context = WearyContext()
        return method_impl(this, context)

    return result