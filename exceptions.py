class MyTypeException(Exception):
    def __init__(self, text):
        super().__init__(text)

class MyZeroException(Exception):
    def __init__(self, text):
        super().__init__(text)

class MyValueException(Exception):
    def __init__(self, text):
        super().__init__(text)
'''
class MyValueException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "MyValueError".format(self.message)
        else:
            return "MyValueError OK"

'''
#raise MyValueException

'''

class MyZeroExeption(Exception):
    def __init__(self, text="Ошбка деления на ноль"):
        super().__init__(text)


raise MyZeroExeption
'''

'''
class MyTypeError(Exception):
    def __init__(self, text="Ввведены не коректные данные"):
        super().__init__(text)


raise MyTypeError("")
'''
