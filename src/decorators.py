from functools import wraps
from typing import Any


def log(filename: Any = None) -> Any:
    """Декоратор, который автоматически логирует начало и конец выполнения функции, а
     также ее результаты или возникшие ошибки."""

    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f"Начало работы функции {func.__name__}")
            try:
                result = func(*args, **kwargs)
                if not filename:
                    print(f"{func.__name__} ok")
                else:
                    with open('mylog.txt', 'a') as file:
                        file.write(f"{func.__name__} ok\n")
                print(f"Конец работы функции {func.__name__}")
                return result
            except Exception as e:
                if filename != "mylog.txt":
                    print(f"{func.__name__} {e}. Inputs: {args}, {kwargs}")
                elif filename == "mylog.txt":
                    with open('mylog.txt', 'a', encoding='utf-8') as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs} \n")
                print(f"Конец работы функции {func.__name__}")
        return wrapper
    return decorator
