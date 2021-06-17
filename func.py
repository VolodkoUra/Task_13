from exceptions import MyTypeException, MyZeroException


def my_sum(x, y):
    if type(x) == int and type(y) == int:
        return x + y
    else:
        raise MyTypeException("Указан не верный тип данных")


def my_dif(x, y):
    if type(x) == int and type(y) == int:
        return x - y
    else:
        raise MyTypeException("Указан не верный тип данных")


def my_mul(x, y):
    if type(x) == int and type(y) == int:
        return x * y
    else:
        raise MyTypeException("Указан не верный тип данных")


def my_division(x, y):
    if type(x) == int and type(y) == int:
        if y == 0:
            raise MyZeroException("Деление на ноль запрещено!")
        else:
            return x / y
    else:
        raise MyTypeException("Указан не верный тип данных")



