class MyClass(Exception):
    pass


class Sub(MyClass):
    pass


class Sub2(MyClass):
    pass


def raiser0():
    x = MyClass()
    raise x


def raiser1():
    x = Sub()
    raise x


def raiser2():
    x = Sub2()
    raise x


# Для чего используются иерархии исключений

class DivZero(Exception):
    pass


class Oflow(Exception):
    pass


def func1():
    raise DivZero


if __name__ == '__main__':
    for func in (raiser0, raiser2, raiser1):
        try:
            func()  # название функцииб коллбэк
        except MyClass:
            import sys
            
            print('захватил: %s' % sys.exc_info()[0])
    
    # Другая реализация
    
    for func in (raiser0, raiser2, raiser1):
        try:
            func()  # название функцииб коллбэк
        except MyClass as X:
            import sys
            
            print('захватил: %s (название класса)' % X.__class__)
    
    # Для чего используются иерархии исключений
    try:
        func1()
    except DivZero as X:
        print('захватил класс %s' % X.__class__)
    except Oflow as y: # до этого класса не доходит
        print('захватил класс %s' % y.__class__)
