

def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if filename != "mylog.txt":
                print(f"{func.__name__} ok")
            elif filename == "mylog.txt":
                with open('mylog.txt', 'a') as file:
                    file.write(f"{func.__name__} ok")


            return result
        return wrapper
    return decorator


@log(filename="mylog.txt")
#@log()
def my_function(x, y):
    return x + y

my_function(1, 2)