# pyright: basic
from time import perf_counter, perf_counter_ns, sleep

from loguru import logger


def timeit(*, use_nanos: bool = False):
    timer = perf_counter if not use_nanos else perf_counter_ns

    def func_wrapper(func):
        def wrapper(*args, **kwargs):
            start = timer()
            func(*args, **kwargs)
            end = timer()
            duration = end - start
            format_options = {
                True: (f"{duration}", "nanoseconds"),
                False: (f"{duration:.1f}", "seconds"),
            }
            formatted_duration, unit = format_options[use_nanos]

            logger.debug(
                f"Function '{func.__name__}' took {formatted_duration} "
                f"{unit} to execute"
            )

        return wrapper

    return func_wrapper


def a_database_operation() -> None:
    sleep(1)


print(timeit())
print(timeit()(a_database_operation))
print(timeit()(a_database_operation)())

timeit()(a_database_operation)()


@timeit(use_nanos=True)
def a_database_operation_with_decorators() -> None:
    sleep(1)


a_database_operation_with_decorators()
