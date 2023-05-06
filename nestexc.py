# Вложенные try, синтаксическое вложение

def action2():
    print(1 + [])


def action1():
    try:
        action2()
    except TypeError:
        print('inner try')

try:
    action1()
except TypeError:
    print('outer try')

# Вложенные try: вложение в потоке управления
try:
    try:
        action2()
    except TypeError:
        print('inner try')
except TypeError:
    print('outer try')
    
# Другой пример вложения, всё завершается, затем вызывается IndexError
"""
try:
    try:
        raise IndexError
    finally:
        print('spam')
finally:
    print('SPAM')
"""
# Прерывание множества вложенных циклов

class ExitLoop (Exception):
    pass

try:
    while True:
        while True:
            for i in range(10):
                if i > 3:
                    raise ExitLoop
                print('loop3: %s' % i)
            print('loop2')
        print('loop1')
except ExitLoop:
    print('countinuing')