# Пример диспетчера контектса

with open(r'data') as myfile:  # базовое использование диспетчера контекста
    for line in myfile:
        print(line)

# Другая реализация

myfile = open('data')

try:
    for line in myfile:
        print(line)
finally:
    myfile.close()


# Протокол упраления контекстами, реализация

class TraceBlock:
    def message(self, arg):
        print('running ' + arg)
    
    def __enter__(self):
        print('starting with block')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception! ' + str(exc_type))
            return False


# Множество диспетчеров контекстов в Python 3.1

with open('data') as fin, open('res', 'w') as fout:
    for line in fin:
        if 'some key' in line:
            fout.write(line)

with open('script1.py') as f1, open('script2.py') as f2:
    for pair in zip(f1, f2):
        print(pair)


with open('script1.py') as f1, open('script2.py') as f2:
    for (lineum1, (line1, line2)) in enumerate(zip(f1, f2)):
        if line1 == line2:
            print('%s\n%r\n%r' % (lineum1, line1, line2))


with open('script2.py') as fin, open('upper.py', 'w') as fout:
    for line in fin:
        fout.write(line.upper())
print(open('upper.py').read())


if __name__ == '__main__':
    with TraceBlock() as action:
        action.message('test 1')
        print('reached')
    with TraceBlock() as action:
        action.message('test 2')
        raise TypeError  # вызвалась ошибка типа
        print('not reached')
