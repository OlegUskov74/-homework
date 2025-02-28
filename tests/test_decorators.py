from src.decorators import log


# @log(filename="mylog.txt")
@log(filename=None)
def my_function(x, y):
    """Функция для тестирования декоратора log"""
    if x > 2:
        raise ValueError("Не правильно введены данные")
    return x + y


def test_log_console_output(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == ('Начало работы функции my_function\n'
                            'my_function ok\n'
                            'Конец работы функции my_function\n')


def test_log_console_output_bug(capsys):
    my_function(3, 2)
    captured = capsys.readouterr()
    assert captured.out == ('Начало работы функции my_function\n'
                            'my_function Не правильно введены данные. Inputs: (3, 2), {}\n'
                            'Конец работы функции my_function\n')


@log(filename="mylog.txt")
def my_function1(x, y):
    """Функция для тестирования декоратора log"""
    if x > 2:
        raise ValueError("Не правильно введены данные")
    return x + y


def test_log_write_to_file(capsys):
    my_function1(1, 2)
    captured = capsys.readouterr()
    assert captured.out == ('Начало работы функции my_function1\n'
                            'Конец работы функции my_function1\n')


def test_log_write_to_file_bug(capsys):
    my_function1(3, 2)
    captured = capsys.readouterr()
    assert captured.out == ('Начало работы функции my_function1\n'
                            'Конец работы функции my_function1\n')
