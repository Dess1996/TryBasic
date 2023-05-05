class MyClass(Exception):
    pass


def myraser():
    raise MyClass


try:
    myraser()
except MyClass:
    print('захватил')
