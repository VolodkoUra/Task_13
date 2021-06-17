from func import my_sum,my_dif,my_mul,my_division
from exceptions import MyZeroException, MyValueException, MyTypeException

def ui_function():
    print("Вас приветствует программа колькулятор!!!")
    while True:
        try:
            x = input("Введите число х: ")
            if not x.isdigit():
                raise MyValueException("Введено не число!")
            y = input("Введите число y: ")
            if not y.isdigit():
                raise MyValueException("Введено не число!")
        except MyValueException as ex:
            print(ex)
            disp =  input("Введите действие которое хотите выполнить:"
                  "\n+ : сложение\n- : вычитание\n* : умножение\n/ : деление\n")
            if disp == "+":
                x = int(x)
                y = int(y)
                print(my_sum(x, y))







ui_function()

