# Стандартное поведение оператора try

def gobad(x, y):
    return x / y


def gosouth(x):
    print(gobad(x, 0))


def kaboom(x, y):
    print(x + y)


# Пример написания кода с помощью try/finally

class MyError(Exception):
    pass


def stuff(file):
    raise MyError()


# Пример: улавливание ограничений (но не ошибок)
def f(x):
    assert x<0, 'x must be negative'
    return x**2



if __name__ == '__main__':
    #    print(gosouth(1))  # стандартная работа скрипта ZeroDivisionError:
#    try:
#        kaboom([0, 1, 2], 'spam')
#    except TypeError:
#        print('Hello, world!')
#    file = open('data', 'w')
    # Пример try-finally
#    try:
#        stuff(file)  # __main__.MyError
#    finally:
#        file.close()

    # Пример унифицированного оператора try

    sep = '-' * 45 + '\n'
    print(sep + 'Исключения генерируются и перехватываются')
    try:
        x = 'spam'[99]
    except IndexError:
        print('except run')
    finally:
        print('finally run')
    print('after run')
    
    print(sep + 'Исключения не генерируются')
    
    try:
        x = 'spam'[2]
    except IndexError:
        print('except run')
    finally:
        print('finally run')
    print('after run')
    
    # Области видимости и переменные except в try
    
    try:
        1/0
    except Exception as X:
        print(X) # перехват имени ошибки
    
    # Распротранение исключений с помощью raise
    
#    try:
#        raise IndexError('spam') # indexError
#    except IndexError:
#        print('propagating')
#        raise

    # Сцепление исключений raise from
    
#    try:
#        1/0
#    except Exception as E:
#        raise TypeError('Bad') from E #Type Error: bad

#    print(sep + 'Исключения генерируются, но не перехватываются')
    
#    try:
#        x = 1/0
#    except IndexError:
#        print('except run')
#    else:
#        print('else run')
#    finally:
#        print('finallly run')
#    print('after run')
    f(1) # x должно быть отрицательным
    
