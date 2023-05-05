def basic_realisation(word, index):
    return word[index]


def indexer(word, index):
    try:
        word[index]
    except IndexError:
        print('Получено исключение')


class MyException(Exception):
    pass


def indexer1(word, index):
    try:
        word[index]
    except IndexError:
        raise MyException ('Написал своё исключение')


indexer('spam', 99)
#basic_realisation('spam', 99)
indexer1('spam', 99)
