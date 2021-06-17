from exceptions import MyZeroException


def my_sum(x, y):
    return "x + y = {}".format(x + y)


def my_dif(x, y):
    return "x - y = {}".format(x - y)


def my_mul(x, y):
    return "x * y = {}".format(x * y)


def my_division(x, y):
    try:
        if y == 0:
            raise MyZeroException("Деление на ноль запрещено!")
        else:
            return "x / y = {}".format(round(x / y, 4))
    except MyZeroException as ex:
        print(ex)
