# pyright: basic
from time import perf_counter, sleep

from loguru import logger


def timeit(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        return_value = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        logger.debug(f"Function '{func.__name__}' took {duration:.1f} seconds")
        return return_value

    return wrapper


def a_database_operation() -> None:
    sleep(1)


timeit(a_database_operation)()


@timeit
def a_database_operation_with_decorators() -> None:
    sleep(2)


a_database_operation_with_decorators()
