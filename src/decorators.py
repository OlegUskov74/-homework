from typing import Any


def log(filename: str | bool = None) -> Any:
    """Декоратор, который автоматически логирует начало и конец выполнения функции, а
     также ее результаты или возникшие ошибки."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Начало работы функции {func.__name__}")
            try:
                result = func(*args, **kwargs)
                if filename != "mylog.txt":
                    print(f"{func.__name__} ok")
                elif filename == "mylog.txt":
                    with open('mylog.txt', 'a') as file:
                        file.write(f"{func.__name__} ok")
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


# if __name__== "__main__":
#
#     #@log(filename="mylog.txt")
#     @log()
#     def my_function(x, y):
#         if x > 2:
#             raise ValueError("Не правильно введены данные")
#         return x + y
#
#
#     my_function(3, 2)
